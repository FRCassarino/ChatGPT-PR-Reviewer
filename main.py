# Import the Chatbot class from the revChatGPT package
from revChatGPT.revChatGPT import Chatbot
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the configuration for the Chatbot
# Replace the placeholder values with your own email, password, and/or session token
config = {
  "session_token":
  "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Xp5021Kvz4P9s4G5.K3LkcIkW4D2AiqUz1QfaAkSTvufPYRWwwnkhI0aBM9RZ426-eR_H0YE6YU9aW2rK4bc3guTYygJqz8M7r8yuXUPhTAT1bJR9YxNmfvgSKYThN1ziji6hPAOolkzXFD5nhBHixUwX3M4OsXr2sCXHvOfaonn3AOj9mJm40u3wyzZSIxLEBYcSPRyVNs11LebeeFLiusHbDzoAOchZPNWwPhiZyyNbGeI-n_gub0tCrTHZnLHxTL1MHq0EtRQujmNeheN1AgCUovqYqZGLFV-_1ZrQigus5pKcQ09P_rSM3gMmA_057TcLs8LIcaazcDbY8Q8IOxPps7c75n-i8w5jx-Oa1DJLx6rgQOsA6Krpkj-HfVc0Mdn0sSvf4EbVXz_W2JsB0sr3g0FWbVlDu43qdmS7cfkGTU0PCXOyp8B9ofqWxEIJiooYzx8_oITkmUWvY0IsWtYUbtvguTwpj-IQENGEli-aWxkrjBHiJTqGOiWHEhkcPU1wsTKwyEfG9Lq4aQGuEqgCa81DGHT0anuGVgF2_FBiUmWbknimpex7xUoVJ6czK2nu-z9-ZzDhORVkqrwxj-n5rYAq7VzZ5tcSAYWsawPDPaU_jpVLGQLJR_2jj-0rZ6GqaNtlo_3I4IdOlpST1ExlqYwKkpCLAK6YgyEbrV3oBczkijD5oC7gEUvWBaj46rBL4BNlHNv-cZBN5hbj0O0Oh20292-X93CpbByfK7yuSyUIxEWBQEGrgAOozeDRy40Iowko0Y1P6XQUHOwq83z-6kEZ-CiWyGeab3Jr0RoTj2tNFV0YK3zmvINAZMK7kmesDhn1alPKtVfgtPIEEUKGZr0UHxlXr3ttA7dAU7LJxXDQmMP7K4Zc53GCSFKqJX-OuzxURHJozsYOsIc9qn9DFpFfuY8o31DA_tEXKMOQWTyTa_7rIquFhsySChfL4xxna5Pqda1Tx9w1hygG_wr9Q-WmXXfy03fZJp74lkDdUuV9xIHtEu4oyNxwwhf5faAZyVYPoW33wEAyLy3vXWhNxOIhPTTvgE56dohKQ46d4Fw9o5sCncvZKa67ihHWdlprUbgYem46I5vIGkVVxMaL9M7eVV_uq1EQ7NH0t-MFQjLtFH5NyAbAMD-LmmdnibApX6Z_PAf9dxLbN7wdTN_zJNtHP_qvSceJepu1fZbrgVQb_76Z92P6LiQCYbD3VIo1hNPXcf5sw61gQpHjkr7uOCKZ-6jgmdoN-Nu3ZJIIMcmkNed0Bngmjsj_BJigYVyacvBwwUuvzntQ8aONAUWy_8YCDjFDqj32ezcCVUtdd_5f7jBzR9LeO_lIkNhR4979ejuWhdkB8Pyt_1dFZ1fLLTAqVM1G0IMr9O4ZVs9qB0u5EEzXxB5o4GFcMZi9Naud1-57_FVWbSV6mL4nPzL4kBAD5YL6rRPDkg5nPtzX2eDSFTUNiF_BdXbrSN4io-Sj_evMxRMiBfY3Exo888M0kXNaoiSKy435N8ULlh_hoiDdbyGYDqLVA8E0Fm8CCjZgcoPGzUZUI6-wXESBYs3t_QbEb9ww_W4kMAJuOC8GWThuMCRmkhsOBchVHYuAf6TaC9W3l4y6RSvQ-GLLn0cSPx39DIIWK5xUnpAs6SZhmk5kB0qJRToPi6gRURyqC5pb-d5C-dQsQRJrSxNkhmX7c33k3V6fCCjjj1jaerKPYZDwdBICftGHPpTYtzoFqF0ybObkduV3yKV8zgDiZaujmj1X-xjF2z3OJXGTP5l_wQCyqwoyzq7gYhnLqsVhhaooVcOZC-4FeqZdeVG-VeeZyXAJ0tCIfPRh-7qFcpi1dYlT4Lpo2SXA1tnl6GT452EUMo9G1omo6GAOzIem20ViY8UD5xKYn4MIkx7-yCOp8W_pgGu6b7jTCzoaGvN86Xd3fcPwSGmfd11wHVShDgjaEqzfjojiRYva6eZpfEWehhxM5-fBGm1j-yJVrb4OIuSIvYJeLbMsfbYWpk6q3KwuSrgAPogmgfwudL06pPo5soOyIWKWd4vPxYywe2zeZj0TYPis8PmHRDKwkTYvoiwfgDOwRSFjnj4GavDnNxe8xDFNwf059YTZ0HiaR1lygS929ZyCF-MrbsWZTN7zmlmetJUm4RNB_AqudJTpq8oycEHqme4I8L2AZ11kKzMhN6zoy_t8-YEAEjg-iQNH_7I3GV19NcnvAiZ1_O71fee2bLG213R8WNBhzmYNl0js0ymnPKqSdYlEQrgMCOSWS-CQjQJxNfZ3XdFe9hTgCUcsCexPTogNaZePlS-19OxaWhnl72iZjvucDoas6L6Dio3dgcR78-x2fReMSjXapx_CubVfrJF5kDcB1aacp40pfNnO1VmLxZZe0mzAw6f0.yxX431KnY2ZB2fuV2KvwtQ"
}

# Initialize the Chatbot with the configuration
chatbot = Chatbot(config)


# Define a function to handle incoming webhooks from the Github App
def handle_webhook(request):
  # Extract the pull request data from the request
  print(request)


request = {
  "action": "closed",
  "number": 1,
  "pull_request": {
    "url": "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1",
    "id": 1152426831,
    "node_id": "PR_kwDOIk6C1s5EsKNP",
    "html_url": "https://github.com/FRCassarino/testPRAI/pull/1",
    "diff_url": "https://github.com/FRCassarino/testPRAI/pull/1.diff",
    "patch_url": "https://github.com/FRCassarino/testPRAI/pull/1.patch",
    "issue_url": "https://api.github.com/repos/FRCassarino/testPRAI/issues/1",
    "number": 1,
    "state": "closed",
    "locked": 0,
    "title": "Create output-2",
    "user": {
      "login": "FRCassarino",
      "id": 6242616,
      "node_id": "MDQ6VXNlcjYyNDI2MTY=",
      "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/FRCassarino",
      "html_url": "https://github.com/FRCassarino",
      "followers_url": "https://api.github.com/users/FRCassarino/followers",
      "following_url":
      "https://api.github.com/users/FRCassarino/following{/other_user}",
      "gists_url": "https://api.github.com/users/FRCassarino/gists{/gist_id}",
      "starred_url":
      "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
      "subscriptions_url":
      "https://api.github.com/users/FRCassarino/subscriptions",
      "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
      "repos_url": "https://api.github.com/users/FRCassarino/repos",
      "events_url":
      "https://api.github.com/users/FRCassarino/events{/privacy}",
      "received_events_url":
      "https://api.github.com/users/FRCassarino/received_events",
      "type": "User",
      "site_admin": 0
    },
    "body": "aasdfdsaf",
    "created_at": "2022-12-07T21:06:23Z",
    "updated_at": "2022-12-08T22:40:17Z",
    "closed_at": "2022-12-08T22:40:17Z",
    "merge_commit_sha": "5a3f0f2465719b93c6f5294cdba0f5d216fc1e7f",
    "assignees": [],
    "requested_reviewers": [],
    "requested_teams": [],
    "commits_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1/commits",
    "review_comments_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1/comments",
    "review_comment_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/pulls/comments{/number}",
    "comments_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/issues/1/comments",
    "statuses_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/statuses/58c2c5972e727f4dbc9992acf1f0cb180bda86af",
    "head": {
      "label": "FRCassarino:test",
      "ref": "test",
      "sha": "58c2c5972e727f4dbc9992acf1f0cb180bda86af",
      "user": {
        "login": "FRCassarino",
        "id": 6242616,
        "node_id": "MDQ6VXNlcjYyNDI2MTY=",
        "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/FRCassarino",
        "html_url": "https://github.com/FRCassarino",
        "followers_url": "https://api.github.com/users/FRCassarino/followers",
        "following_url":
        "https://api.github.com/users/FRCassarino/following{/other_user}",
        "gists_url":
        "https://api.github.com/users/FRCassarino/gists{/gist_id}",
        "starred_url":
        "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
        "subscriptions_url":
        "https://api.github.com/users/FRCassarino/subscriptions",
        "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
        "repos_url": "https://api.github.com/users/FRCassarino/repos",
        "events_url":
        "https://api.github.com/users/FRCassarino/events{/privacy}",
        "received_events_url":
        "https://api.github.com/users/FRCassarino/received_events",
        "type": "User",
      },
      "repo": {
        "id": 575570646,
        "node_id": "R_kgDOIk6C1g",
        "name": "testPRAI",
        "full_name": "FRCassarino/testPRAI",
        "owner": {
          "login": "FRCassarino",
          "id": 6242616,
          "node_id": "MDQ6VXNlcjYyNDI2MTY=",
          "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/FRCassarino",
          "html_url": "https://github.com/FRCassarino",
          "followers_url":
          "https://api.github.com/users/FRCassarino/followers",
          "following_url":
          "https://api.github.com/users/FRCassarino/following{/other_user}",
          "gists_url":
          "https://api.github.com/users/FRCassarino/gists{/gist_id}",
          "starred_url":
          "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
          "subscriptions_url":
          "https://api.github.com/users/FRCassarino/subscriptions",
          "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
          "repos_url": "https://api.github.com/users/FRCassarino/repos",
          "events_url":
          "https://api.github.com/users/FRCassarino/events{/privacy}",
          "received_events_url":
          "https://api.github.com/users/FRCassarino/received_events",
          "type": "User",
        },
        "url": "https://api.github.com/repos/FRCassarino/testPRAI",
        "forks_url": "https://api.github.com/repos/FRCassarino/testPRAI/forks",
        "keys_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/keys{/key_id}",
        "collaborators_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/FRCassarino/testPRAI/teams",
        "hooks_url": "https://api.github.com/repos/FRCassarino/testPRAI/hooks",
        "issue_events_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues/events{/number}",
        "events_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/events",
        "assignees_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/assignees{/user}",
        "branches_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/branches{/branch}",
        "tags_url": "https://api.github.com/repos/FRCassarino/testPRAI/tags",
        "blobs_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/blobs{/sha}",
        "git_tags_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/tags{/sha}",
        "git_refs_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/refs{/sha}",
        "trees_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/trees{/sha}",
        "statuses_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/statuses/{sha}",
        "languages_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/languages",
        "stargazers_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/stargazers",
        "contributors_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/contributors",
        "subscribers_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/subscribers",
        "subscription_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/subscription",
        "commits_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/commits{/sha}",
        "git_commits_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/commits{/sha}",
        "comments_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/comments{/number}",
        "issue_comment_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues/comments{/number}",
        "contents_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/contents/{+path}",
        "compare_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/compare/{base}...{head}",
        "merges_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/merges",
        "archive_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/{archive_format}{/ref}",
        "downloads_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/downloads",
        "issues_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues{/number}",
        "pulls_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/pulls{/number}",
        "milestones_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/milestones{/number}",
        "notifications_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/notifications{?since,all,participating}",
        "labels_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/labels{/name}",
        "releases_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/releases{/id}",
        "deployments_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/deployments",
        "created_at": "2022-12-07T20:13:34Z",
        "updated_at": "2022-12-07T20:13:34Z",
        "pushed_at": "2022-12-07T21:06:23Z",
        "git_url": "git://github.com/FRCassarino/testPRAI.git",
        "ssh_url": "git@github.com:FRCassarino/testPRAI.git",
        "clone_url": "https://github.com/FRCassarino/testPRAI.git",
        "svn_url": "https://github.com/FRCassarino/testPRAI",
        "size": 315,
        "stargazers_count": 0,
        "watchers_count": 0,
        "squash_merge_commit_message": "COMMIT_MESSAGES",
        "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
        "merge_commit_message": "PR_TITLE",
        "merge_commit_title": "MERGE_MESSAGE"
      }
    },
    "base": {
      "label": "FRCassarino:main",
      "ref": "main",
      "sha": "3406b7c255f72d81d8c648a55c3666b7b00e86fb",
      "user": {
        "login": "FRCassarino",
        "id": 6242616,
        "node_id": "MDQ6VXNlcjYyNDI2MTY=",
        "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/FRCassarino",
        "html_url": "https://github.com/FRCassarino",
        "followers_url": "https://api.github.com/users/FRCassarino/followers",
        "following_url":
        "https://api.github.com/users/FRCassarino/following{/other_user}",
        "gists_url":
        "https://api.github.com/users/FRCassarino/gists{/gist_id}",
        "starred_url":
        "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
        "subscriptions_url":
        "https://api.github.com/users/FRCassarino/subscriptions",
        "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
        "repos_url": "https://api.github.com/users/FRCassarino/repos",
        "events_url":
        "https://api.github.com/users/FRCassarino/events{/privacy}",
        "received_events_url":
        "https://api.github.com/users/FRCassarino/received_events",
        "type": "User",
      },
      "repo": {
        "id": 575570646,
        "node_id": "R_kgDOIk6C1g",
        "name": "testPRAI",
        "full_name": "FRCassarino/testPRAI",
        "owner": {
          "login": "FRCassarino",
          "id": 6242616,
          "node_id": "MDQ6VXNlcjYyNDI2MTY=",
          "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/FRCassarino",
          "html_url": "https://github.com/FRCassarino",
          "followers_url":
          "https://api.github.com/users/FRCassarino/followers",
          "following_url":
          "https://api.github.com/users/FRCassarino/following{/other_user}",
          "gists_url":
          "https://api.github.com/users/FRCassarino/gists{/gist_id}",
          "starred_url":
          "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
          "subscriptions_url":
          "https://api.github.com/users/FRCassarino/subscriptions",
          "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
          "repos_url": "https://api.github.com/users/FRCassarino/repos",
          "events_url":
          "https://api.github.com/users/FRCassarino/events{/privacy}",
          "received_events_url":
          "https://api.github.com/users/FRCassarino/received_events",
          "type": "User",
        },
        "html_url": "https://github.com/FRCassarino/testPRAI",
        "url": "https://api.github.com/repos/FRCassarino/testPRAI",
        "forks_url": "https://api.github.com/repos/FRCassarino/testPRAI/forks",
        "keys_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/keys{/key_id}",
        "collaborators_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/FRCassarino/testPRAI/teams",
        "hooks_url": "https://api.github.com/repos/FRCassarino/testPRAI/hooks",
        "issue_events_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues/events{/number}",
        "events_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/events",
        "assignees_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/assignees{/user}",
        "branches_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/branches{/branch}",
        "tags_url": "https://api.github.com/repos/FRCassarino/testPRAI/tags",
        "blobs_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/blobs{/sha}",
        "git_tags_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/tags{/sha}",
        "git_refs_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/refs{/sha}",
        "trees_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/trees{/sha}",
        "statuses_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/statuses/{sha}",
        "languages_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/languages",
        "stargazers_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/stargazers",
        "contributors_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/contributors",
        "subscribers_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/subscribers",
        "subscription_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/subscription",
        "commits_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/commits{/sha}",
        "git_commits_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/git/commits{/sha}",
        "comments_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/comments{/number}",
        "issue_comment_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues/comments{/number}",
        "contents_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/contents/{+path}",
        "compare_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/compare/{base}...{head}",
        "merges_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/merges",
        "archive_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/{archive_format}{/ref}",
        "downloads_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/downloads",
        "issues_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues{/number}",
        "pulls_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/pulls{/number}",
        "milestones_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/milestones{/number}",
        "notifications_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/notifications{?since,all,participating}",
        "labels_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/labels{/name}",
        "releases_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/releases{/id}",
        "deployments_url":
        "https://api.github.com/repos/FRCassarino/testPRAI/deployments",
        "created_at": "2022-12-07T20:13:34Z",
        "updated_at": "2022-12-07T20:13:34Z",
        "pushed_at": "2022-12-07T21:06:23Z",
        "git_url": "git://github.com/FRCassarino/testPRAI.git",
        "ssh_url": "git@github.com:FRCassarino/testPRAI.git",
        "clone_url": "https://github.com/FRCassarino/testPRAI.git",
        "svn_url": "https://github.com/FRCassarino/testPRAI",
        "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
        "merge_commit_message": "PR_TITLE",
        "merge_commit_title": "MERGE_MESSAGE"
      }
    },
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1"
      },
      "html": {
        "href": "https://github.com/FRCassarino/testPRAI/pull/1"
      },
      "issue": {
        "href": "https://api.github.com/repos/FRCassarino/testPRAI/issues/1"
      },
      "comments": {
        "href":
        "https://api.github.com/repos/FRCassarino/testPRAI/issues/1/comments"
      },
      "review_comments": {
        "href":
        "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1/comments"
      },
      "review_comment": {
        "href":
        "https://api.github.com/repos/FRCassarino/testPRAI/pulls/comments{/number}"
      },
      "commits": {
        "href":
        "https://api.github.com/repos/FRCassarino/testPRAI/pulls/1/commits"
      },
      "statuses": {
        "href":
        "https://api.github.com/repos/FRCassarino/testPRAI/statuses/58c2c5972e727f4dbc9992acf1f0cb180bda86af"
      }
    },
    "author_association": "OWNER",
    "commits": 1,
    "additions": 0,
    "deletions": 0,
    "changed_files": 1
  },
  "repository": {
    "id": 575570646,
    "node_id": "R_kgDOIk6C1g",
    "name": "testPRAI",
    "full_name": "FRCassarino/testPRAI",
    "owner": {
      "login": "FRCassarino",
      "id": 6242616,
      "node_id": "MDQ6VXNlcjYyNDI2MTY=",
      "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/FRCassarino",
      "html_url": "https://github.com/FRCassarino",
      "followers_url": "https://api.github.com/users/FRCassarino/followers",
      "following_url":
      "https://api.github.com/users/FRCassarino/following{/other_user}",
      "gists_url": "https://api.github.com/users/FRCassarino/gists{/gist_id}",
      "starred_url":
      "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
      "subscriptions_url":
      "https://api.github.com/users/FRCassarino/subscriptions",
      "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
      "repos_url": "https://api.github.com/users/FRCassarino/repos",
      "events_url":
      "https://api.github.com/users/FRCassarino/events{/privacy}",
      "received_events_url":
      "https://api.github.com/users/FRCassarino/received_events",
      "type": "User",
    },
    "html_url": "https://github.com/FRCassarino/testPRAI",
    "url": "https://api.github.com/repos/FRCassarino/testPRAI",
    "forks_url": "https://api.github.com/repos/FRCassarino/testPRAI/forks",
    "keys_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/keys{/key_id}",
    "collaborators_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/FRCassarino/testPRAI/teams",
    "hooks_url": "https://api.github.com/repos/FRCassarino/testPRAI/hooks",
    "issue_events_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/issues/events{/number}",
    "events_url": "https://api.github.com/repos/FRCassarino/testPRAI/events",
    "assignees_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/assignees{/user}",
    "branches_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/branches{/branch}",
    "tags_url": "https://api.github.com/repos/FRCassarino/testPRAI/tags",
    "blobs_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/git/blobs{/sha}",
    "git_tags_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/git/tags{/sha}",
    "git_refs_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/git/refs{/sha}",
    "trees_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/git/trees{/sha}",
    "statuses_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/statuses/{sha}",
    "languages_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/languages",
    "stargazers_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/stargazers",
    "contributors_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/contributors",
    "subscribers_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/subscribers",
    "subscription_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/subscription",
    "commits_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/commits{/sha}",
    "git_commits_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/git/commits{/sha}",
    "comments_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/comments{/number}",
    "issue_comment_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/issues/comments{/number}",
    "contents_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/contents/{+path}",
    "compare_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/FRCassarino/testPRAI/merges",
    "archive_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/{archive_format}{/ref}",
    "downloads_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/downloads",
    "issues_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/issues{/number}",
    "pulls_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/pulls{/number}",
    "milestones_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/milestones{/number}",
    "notifications_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/notifications{?since,all,participating}",
    "labels_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/labels{/name}",
    "releases_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/releases{/id}",
    "deployments_url":
    "https://api.github.com/repos/FRCassarino/testPRAI/deployments",
    "created_at": "2022-12-07T20:13:34Z",
    "updated_at": "2022-12-07T20:13:34Z",
    "pushed_at": "2022-12-07T21:06:23Z",
    "git_url": "git://github.com/FRCassarino/testPRAI.git",
    "ssh_url": "git@github.com:FRCassarino/testPRAI.git",
    "clone_url": "https://github.com/FRCassarino/testPRAI.git",
    "svn_url": "https://github.com/FRCassarino/testPRAI",
    "topics": [],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "test"
  },
  "sender": {
    "login": "FRCassarino",
    "id": 6242616,
    "node_id": "MDQ6VXNlcjYyNDI2MTY=",
    "avatar_url": "https://avatars.githubusercontent.com/u/6242616?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/FRCassarino",
    "html_url": "https://github.com/FRCassarino",
    "followers_url": "https://api.github.com/users/FRCassarino/followers",
    "following_url":
    "https://api.github.com/users/FRCassarino/following{/other_user}",
    "gists_url": "https://api.github.com/users/FRCassarino/gists{/gist_id}",
    "starred_url":
    "https://api.github.com/users/FRCassarino/starred{/owner}{/repo}",
    "subscriptions_url":
    "https://api.github.com/users/FRCassarino/subscriptions",
    "organizations_url": "https://api.github.com/users/FRCassarino/orgs",
    "repos_url": "https://api.github.com/users/FRCassarino/repos",
    "events_url": "https://api.github.com/users/FRCassarino/events{/privacy}",
    "received_events_url":
    "https://api.github.com/users/FRCassarino/received_events",
    "type": "User",
  },
  "installation": {
    "id": 31969756,
    "node_id": "MDIzOkludGVncmF0aW9uSW5zdGFsbGF0aW9uMzE5Njk3NTY="
  }
}


# Define a request handler class that passes incoming requests to the handle_webhook function
class RequestHandler(BaseHTTPRequestHandler):

  def do_POST(self):
    # Parse the request data
    data = self.rfile.read(int(self.headers["Content-Length"])).decode()

    # Pass the request data to the handle_webhook function
    handle_webhook(data)

    # Send a 200 OK response
    self.send_response(200)
    self.end_headers()


# Create an HTTPServer that listens for incoming requests on localhost port 80
server = HTTPServer(("localhost", 80), RequestHandler)

# Start the server in an infinite loop
while True:
  server.handle_request()
