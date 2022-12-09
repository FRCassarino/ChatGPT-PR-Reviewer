import base64
import json
import requests
from patch import fromstring
import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler


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
            path = str(filename).split('/')[1]
            path = path.replace("'", "")
           
            # Use the GitHub API to get the contents of the modified file
            url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
            headers = {'Authorization': 'token <YOUR_AUTH_TOKEN>'}
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


httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()


