from ast import List
import base64
import json
import re
import requests
from patch import fromstring
import urllib
from revChatGPT.revChatGPT import Chatbot


from http.server import HTTPServer, BaseHTTPRequestHandler

# Load the configuration from the JSON file
with open('config.json', 'r') as config_file:
  config = json.load(config_file)

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Get the length of the request body
        content_length = int(self.headers['Content-Length'])
        
        # Read the request body
        body = self.rfile.read(content_length)
        
        # Handle the webhook
        self.handle_webhook(body)
        
        # Send a response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Received POST request")

    def handle_webhook(self, body):
        # Decode the request body
        data = body.decode('utf-8')

        # Parse the data as a JSON object
        try:
            data = json.loads(data)  
        except json.decoder.JSONDecodeError as err:
            print(f'Error parsing JSON: {err}')
            
            return

        # Extract the pull request information from the data
        pull_request = data['pull_request']

        # Create the modified files array
        modified_files = self.create_modified_files_array(pull_request)

        # Review the pull request
        review = self.review_pull_request(modified_files)
        print("Review: " + review)

        # Post the review as a comment in the pull request
        self.post_review_as_comment(review, pull_request)

    def create_modified_files_array(self, pull_request):
        # Initialize the modified files array
        modified_files = []

        # Get the URL of the patch file for the pull request
        patch_url = pull_request['patch_url']

        # Download the patch file from the URL
        patch_file = urllib.request.urlopen(patch_url)

        # Parse the patch file using the Patch class
        patch_set = fromstring(patch_file.read())

        # Get the repository information from the pull request
        repo = pull_request['head']['repo']['name']
        owner = pull_request['user']['login']

        for patch in patch_set:

            filename = patch.target.decode('utf-8')
            
            # Use the GitHub API to get the contents of the modified file
            url = f'https://api.github.com/repos/{owner}/{repo}/contents/main.py'
            headers = {'Authorization': 'token ' + config["github_token"]}
            try:
                response = requests.get(url, headers=headers)
                data = response.json()
            except requests.RequestException as err:
                print(f'Error making request to GitHub API: {err}')
                return

            # Decode the base64 encoded content of the file
            code = base64.b64decode(data['content']).decode('utf-8').splitlines()

            numbered_code = [f'{i+1} {line}' for i, line in enumerate(code)] 

            # Add the filename and code to the modified files array
            modified_files.append("File: " + filename + "\n" + "\n".join(numbered_code))

        return modified_files

    def review_pull_request(self, modified_files):
      # Create a Chatbot instance
      chatbot = Chatbot(config)

      chatbot.get_chat_response("We're going to do an exercise. Imagine these are a series of coding files that belong to a Github Pull Request. Please simply write ACKNOWLEDGE, and write a short summary of what each file does. I will send the first file after this message. Please respond now with ACKNOWLEDGE", output="text")

      # Send the modified files to the chatbot
      for file in modified_files:
          print(chatbot.get_chat_response(file, output="text"))

      # Ask the chatbot to review the pull request
      review = chatbot.get_chat_response("For the code I pasted, find code smells or questionable technical decisions, identify bugs and explain issues. \nStructure this as a list of items, ranked by importance. Each item should be in the format [<FILENAME>, <LINE_OF_CODE>]: <ITEM_TEXT>. \nThis does NOT require you to browse  the internet or analyze specific code files.", output="text")
    
      # Return the chatbot's review
      return review['message']

    def post_review_as_comment(self, review, pull_request):
      # Get the repository information from the pull request
      repo = pull_request['head']['repo']['name']
      owner = pull_request['user']['login']
      number = pull_request['number']

      # Set the URL for creating a new comment on the pull request
      url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{number}'
      lines = review.split('\n')

      # Compile a regular expression to match the file and line number pattern
      pattern = re.compile(r'\[(.+), line (\d+)\]:')

      for line in lines:
        # Check if the line is a comment
        if pattern.match(line):
            # Extract the file and line number from the line
            file, line_number = pattern.findall(line)[0]

            # Use the GitHub API to post the comment in the specified file and line
            comment_url = f'{url}/comments'
            body = {
                'body': line,
                'commit_id': pull_request['head']['sha'],
                'path': file,
                'line': int(line_number),
            }
            headers = {'Authorization': 'token ' + config["github_token"]}
            try:
                response = requests.post(comment_url, json=body, headers=headers)
            except requests.RequestException as err:
                print(f'Error posting comment: {err}')
                return

httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()


