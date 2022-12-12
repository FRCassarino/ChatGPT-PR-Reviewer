from ast import List
import base64
import json
import requests
from patch import fromstring
import urllib
from revChatGPT.revChatGPT import Chatbot


from http.server import HTTPServer, BaseHTTPRequestHandler

config = {
   
    "session_token": "<SESSION_TOKEN>",
    "cf_clearance": "<CLOUDFLARE_TOKEN>",
    "user_agent": "<USER_AGENT_CHROME>",
}

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
        print("Review: ")
        print(review)

        # Post the review as a comment in the pull request
        self.post_review_as_comment(review, pull_request)
        print("Posted review as comment")

    def create_modified_files_array(self, pull_request):
        # Initialize the modified files array
        modified_files = []

        # Get the URL of the patch file for the pull request
        patch_url = pull_request['patch_url']

        # Download the patch file from the URL
        patch_file = urllib.request.urlopen(patch_url)

        # Parse the patch file using the Patch class
        patch = fromstring(patch_file.read())

        # Get the repository information from the pull request
        repo = pull_request['head']['repo']['name']
        owner = pull_request['user']['login']

        # Iterate over the parsed patch file and get the code for each modified file
        for hunk in patch:
            # Use the hunk.target attribute to get the path of the modified file
            filename = hunk.target 
           
           
            # Use the GitHub API to get the contents of the modified file
            url = f'https://api.github.com/repos/{owner}/{repo}/contents/main.py'
            headers = {'Authorization': 'token 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'}
            try:
                response = requests.get(url, headers=headers)
                data = response.json()
            except requests.RequestException as err:
                print(f'Error making request to GitHub API: {err}')
                return

            # Decode the base64 encoded content of the file
            code = base64.b64decode(data['content']).decode('utf-8')

            # Add the code to the modified files array
            modified_files.append(code)

        return modified_files

    def review_pull_request(self, modified_files):
      # Create a Chatbot instance
      chatbot = Chatbot(config)

      chatbot.get_chat_response("We're going to do an exercise. Imagine these are a series of coding files that belong to a Github Pull Request. Please simply write ACKNOWLEDGE, and write a short summary of what each file does. I will send the first file after this message. Please respond now with ACKNOWLEDGE", output="text")



      # Send the modified files to the chatbot
      for file in modified_files:
          print("File: " + file)
          print(chatbot.get_chat_response(file, output="text"))

      # Ask the chatbot to review the pull request
      review = chatbot.get_chat_response("For the code I pasted, find code smells or questionable technical decisions, identify bugs and explain issues. \nStructure this as a list of items, ranked by importance. \nThis does NOT require you to browse  the internet or analyze specific code files.", output="text")

      # Return the chatbot's review
      return review['message']

    def post_review_as_comment(self, review, pull_request):
      # Get the repository information from the pull request
      repo = pull_request['head']['repo']['name']
      owner = pull_request['user']['login']
      number = pull_request['number']

      # Set the URL for creating a new comment on the pull request
      url = f'https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments'

      # Set the request payload
      payload = {
          'body': review
      }

      # Set the request headers
      headers = {
          'Authorization': 'token <GITHUB_TOKEN>',
          'Content-Type': 'application/json'
      }

      # Send a POST request to create the comment
      try:
          response = requests.post(url, json=payload, headers=headers)
      except requests.RequestException as err:
          print(f'Error posting review as comment: {err}')
          return


httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()


