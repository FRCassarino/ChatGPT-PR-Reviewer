import base64
import json
import re
import requests
from patch import fromstring
import urllib
from revChatGPT.revChatGPT import Chatbot
from github_api import GitHubAPI
import os


# Load the configuration from the JSON file
with open('config.json', 'r') as config_file:
  local_config = json.load(config_file)

config = {
    "github_token": os.environ.get('GITHUB_TOKEN') or local_config['github_token'],
    "session_token": os.environ.get('SESSION_TOKEN') or local_config['session_token'],
    "user_agent": os.environ.get('USER_AGENT') or local_config['user_agent'],
    "cf_clearance": os.environ.get('CF_CLEARANCE') or local_config['cf_clearance'],
}

mock_review = "[app.py, line 10]: The value of the session_token key in the config dictionary is not defined.\n[app.py, line 24]: The send_response method is called with a hardcoded value of 200. It is better to use one of the pre-defined constants from the http.server module, such as HTTPStatus.OK, instead of a hardcoded value.\n[app.py, line 25]: The end_headers method is called after the response has been sent, but it should be called before the response is sent.\n[app.py, line 27]: The write method is used to write the response body, but it should be used with a binary string, not a regular string. The string needs to be encoded as binary before it is written to the response.\n[app.py, line 45]: The modified_files array is printed to the console, but it is not used anywhere else in the code. It would be better to either use it in another part of the code, or remove it entirely.\n[app.py, line 60]: The patch_file variable is assigned the result of calling the get method from the requests module, but this variable is never used in the code. It would be better to either use this variable, or remove the assignment statement.\n[app.py, line 75]: There is no return statement in the create_modified_files_array method, so the method will always return None. It would be better to either add a return statement at the end of the method, or change the method to be a void method."
should_mock = True
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
        review = mock_review if should_mock else self.generate_review(changed_files)

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

    
    
