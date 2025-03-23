import os
import requests
import base64


def get_subdirs(directory):
    subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    return subdirs

def get_github_file_content(owner, repo, path, branch='main', token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json()['content']
        return base64.b64decode(content).decode('utf-8')
    else:
        return None