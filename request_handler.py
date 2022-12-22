import base64
import json
import re
import requests
from patch import fromstring
import urllib
from revChatGPT.revChatGPT import Chatbot
from github_api import GitHubAPI

# Load the configuration from the JSON file
with open('config.json', 'r') as config_file:
  config = json.load(config_file)


class RequestHandler:
    def handle_webhook(self, body):

        # Parse the data as a JSON object
        try:
            data = json.loads(body)  
        except json.decoder.JSONDecodeError as err:
            print(f'Error parsing JSON: {err}')
            return

        # Extract the pull request information from the data
        pull_request = data['pull_request']

        # The full files changed in the pull request
        changed_files = self.changed_files(pull_request)

        # Use ChatGPT to generate a review for the pull request
        review = self.generate_review(changed_files)
        print("Pull Request Review: " + review)

        # Post the review as a comment in the pull request
        self.post_review(review, pull_request)

    def changed_files(self, pull_request):
        # Initialize the changed files array
        changed_files = []

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
            
            # Use the GitHub API to get the contents of the changed file
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

            # Add the filename and code to the changed files array
            changed_files.append("File: " + filename + "\n" + "\n".join(numbered_code))

        return changed_files

    def generate_review(self, changed_files):
      # Create a Chatbot instance
      chatbot = Chatbot(config)

      chatbot.get_chat_response("We're going to do an exercise. Imagine these are a series of coding files that belong to a Github Pull Request. Please simply write ACKNOWLEDGE, and write a short summary of what each file does. I will send the first file after this message. Please respond now with ACKNOWLEDGE", output="text")

      # Send the changed files to the chatbot
      for file in changed_files:
          print(chatbot.get_chat_response(file, output="text"))

      # Ask the chatbot to review the pull request
      review = chatbot.get_chat_response("For the code I pasted, find code smells or questionable technical decisions, identify bugs and explain issues. \nStructure this as a list of items. Each item should be in the format [<FILENAME>, <LINE_OF_CODE>]: <ITEM_TEXT>. \nThis does NOT require you to browse  the internet or analyze specific code files.", output="text")
    
      # Return the chatbot's review
      return review['message']

    def post_review(self, review, pull_request):
    
      github_api = GitHubAPI(config["github_token"])

      lines = review.split('\n')

      # Compile a regular expression to match the file and line number pattern
      pattern = re.compile(r'\[(.+), line (\d+)\]:')

      for line in lines:
        # Check if the line is a comment
        if pattern.match(line):
            # Extract the file and line number from the line
            file, line_number = pattern.findall(line)[0]            
            github_api.post_review_item_as_comment(line, pull_request, file, line_number)