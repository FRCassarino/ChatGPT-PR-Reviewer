import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
import requests
from patch import fromstring
import urllib

# Define the configuration for the Chatbot
# Replace the placeholder values with your own email, password, and/or session token
config = {
  "session_token":
  "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Xp5021Kvz4P9s4G5.K3LkcIkW4D2AiqUz1QfaAkSTvufPYRWwwnkhI0aBM9RZ426-eR_H0YE6YU9aW2rK4bc3guTYygJqz8M7r8yuXUPhTAT1bJR9YxNmfvgSKYThN1ziji6hPAOolkzXFD5nhBHixUwX3M4OsXr2sCXHvOfaonn3AOj9mJm40u3wyzZSIxLEBYcSPRyVNs11LebeeFLiusHbDzoAOchZPNWwPhiZyyNbGeI-n_gub0tCrTHZnLHxTL1MHq0EtRQujmNeheN1AgCUovqYqZGLFV-_1ZrQigus5pKcQ09P_rSM3gMmA_057TcLs8LIcaazcDbY8Q8IOxPps7c75n-i8w5jx-Oa1DJLx6rgQOsA6Krpkj-HfVc0Mdn0sSvf4EbVXz_W2JsB0sr3g0FWbVlDu43qdmS7cfkGTU0PCXOyp8B9ofqWxEIJiooYzx8_oITkmUWvY0IsWtYUbtvguTwpj-IQENGEli-aWxkrjBHiJTqGOiWHEhkcPU1wsTKwyEfG9Lq4aQGuEqgCa81DGHT0anuGVgF2_FBiUmWbknimpex7xUoVJ6czK2nu-z9-ZzDhORVkqrwxj-n5rYAq7VzZ5tcSAYWsawPDPaU_jpVLGQLJR_2jj-0rZ6GqaNtlo_3I4IdOlpST1ExlqYwKkpCLAK6YgyEbrV3oBczkijD5oC7gEUvWBaj46rBL4BNlHNv-cZBN5hbj0O0Oh20292-X93CpbByfK7yuSyUIxEWBQEGrgAOozeDRy40Iowko0Y1P6XQUHOwq83z-6kEZ-CiWyGeab3Jr0RoTj2tNFV0YK3zmvINAZMK7kmesDhn1alPKtVfgtPIEEUKGZr0UHxlXr3ttA7dAU7LJxXDQmMP7K4Zc53GCSFKqJX-OuzxURHJozsYOsIc9qn9DFpFfuY8o31DA_tEXKMOQWTyTa_7rIquFhsySChfL4xxna5Pqda1Tx9w1hygG_wr9Q-WmXXfy03fZJp74lkDdUuV9xIHtEu4oyNxwwhf5faAZyVYPoW33wEAyLy3vXWhNxOIhPTTvgE56dohKQ46d4Fw9o5sCncvZKa67ihHWdlprUbgYem46I5vIGkVVxMaL9M7eVV_uq1EQ7NH0t-MFQjLtFH5NyAbAMD-LmmdnibApX6Z_PAf9dxLbN7wdTN_zJNtHP_qvSceJepu1fZbrgVQb_76Z92P6LiQCYbD3VIo1hNPXcf5sw61gQpHjkr7uOCKZ-6jgmdoN-Nu3ZJIIMcmkNed0Bngmjsj_BJigYVyacvBwwUuvzntQ8aONAUWy_8YCDjFDqj32ezcCVUtdd_5f7jBzR9LeO_lIkNhR4979ejuWhdkB8Pyt_1dFZ1fLLTAqVM1G0IMr9O4ZVs9qB0u5EEzXxB5o4GFcMZi9Naud1-57_FVWbSV6mL4nPzL4kBAD5YL6rRPDkg5nPtzX2eDSFTUNiF_BdXbrSN4io-Sj_evMxRMiBfY3Exo888M0kXNaoiSKy435N8ULlh_hoiDdbyGYDqLVA8E0Fm8CCjZgcoPGzUZUI6-wXESBYs3t_QbEb9ww_W4kMAJuOC8GWThuMCRmkhsOBchVHYuAf6TaC9W3l4y6RSvQ-GLLn0cSPx39DIIWK5xUnpAs6SZhmk5kB0qJRToPi6gRURyqC5pb-d5C-dQsQRJrSxNkhmX7c33k3V6fCCjjj1jaerKPYZDwdBICftGHPpTYtzoFqF0ybObkduV3yKV8zgDiZaujmj1X-xjF2z3OJXGTP5l_wQCyqwoyzq7gYhnLqsVhhaooVcOZC-4FeqZdeVG-VeeZyXAJ0tCIfPRh-7qFcpi1dYlT4Lpo2SXA1tnl6GT452EUMo9G1omo6GAOzIem20ViY8UD5xKYn4MIkx7-yCOp8W_pgGu6b7jTCzoaGvN86Xd3fcPwSGmfd11wHVShDgjaEqzfjojiRYva6eZpfEWehhxM5-fBGm1j-yJVrb4OIuSIvYJeLbMsfbYWpk6q3KwuSrgAPogmgfwudL06pPo5soOyIWKWd4vPxYywe2zeZj0TYPis8PmHRDKwkTYvoiwfgDOwRSFjnj4GavDnNxe8xDFNwf059YTZ0HiaR1lygS929ZyCF-MrbsWZTN7zmlmetJUm4RNB_AqudJTpq8oycEHqme4I8L2AZ11kKzMhN6zoy_t8-YEAEjg-iQNH_7I3GV19NcnvAiZ1_O71fee2bLG213R8WNBhzmYNl0js0ymnPKqSdYlEQrgMCOSWS-CQjQJxNfZ3XdFe9hTgCUcsCexPTogNaZePlS-19OxaWhnl72iZjvucDoas6L6Dio3dgcR78-x2fReMSjXapx_CubVfrJF5kDcB1aacp40pfNnO1VmLxZZe0mzAw6f0.yxX431KnY2ZB2fuV2KvwtQ"
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


        print("Received POST request")

        # Parse the data as a JSON object
        data = json.loads(data)  

        # Extract the pull request information from the data
        pull_request = data['pull_request']

        # Create the modified files array
        modified_files = self.create_modified_files_array(pull_request)
    
        return modified_files

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
            print(hunk.target)
            filename = hunk.target 
            path = str(filename).split('/')[1]
            path = path.replace("'", "")
            print('path is :' +  path)
           
            # Use the GitHub API to get the contents of the modified file
            url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
            print(url)
            headers = {'Authorization': f'token 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'}
            response = requests.get(url, headers=headers)
            data = response.json()
            # Decode the base64 encoded content of the file
            code = base64.b64decode(data['content']).decode('utf-8')
            print(code)

            # Add the code to the modified files array
            modified_files.append(code)

        return modified_files


httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()


