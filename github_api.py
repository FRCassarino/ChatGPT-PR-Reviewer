import json
import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token

    def post_review_item_as_comment(self, reviewItem, pull_request, file, line_number):
        # Get the repository information from the pull request
        repo = pull_request['head']['repo']['name']
        owner = pull_request['user']['login']
        number = pull_request['number']
        # Set the URL for creating a new comment on the pull request
        comment_url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{number}/comments'

        # Set the request headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'token {self.token}'
        }

        # Set the request body
        body = {
                'body': reviewItem,
                'commit_id': pull_request['head']['sha'],
                'path': file,
                'line': int(line_number),
            }

        try:
            # Make a POST request to the comments endpoint
            requests.post(comment_url, headers=headers, data=body)
        except requests.RequestException as err:
            print(f'Error posting review item as comment: {err}')
            return
