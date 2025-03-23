from Plugins.TwitchConnector import misc
import os

FILES = [
    "main.pyw",
    "misc.py",
    "updater.py"
]

def compare_files(owner, repo, path, branch='main', token=None):
    local_file = open(path, 'r').read()
    remote_file = misc.get_github_file_content(owner, repo, path, branch, token)
    return local_file == remote_file

def update_file(owner, repo, path, branch='main', token=None):
    print("Updating file:", path)
    with open(os.environ["LOG_FILE"], "a") as f:
        print("Updating file:", path, file=f)
    if compare_files(owner, repo, path, branch, token):
        print("    File is up to date.")
        with open(os.environ["LOG_FILE"], "a") as f:
            print("    File is already up to date.", file=f)
    else:
        print("    File is outdated, updating...")
        with open(os.environ["LOG_FILE"], "a") as f:
            print("    File is outdated, updating...", file=f)
        remote_file = misc.get_github_file_content(owner, repo, path, branch, token)
        with open(path, 'w') as f:
            f.write(remote_file)
        print("    File updated.")
        with open(os.environ["LOG_FILE"], "a") as f:
            print("    File updated.", file=f)

def update_all(owner, repo):
    print("Checking for updates...")
    with open(os.environ["LOG_FILE"], "a") as f:
        print("Checking for updates", file=f)
    update = False
    needs_to_update = []
    for file in FILES:
        if not compare_files("EclipseShadow55", "WireBox", file):
            needs_to_update.append(file)
            with open(os.environ["LOG_FILE"], "a") as f:
                print("Update needed for", file, file=f)
    if len(needs_to_update):
        if input("Would you like to update all programs (y/n): ").lower()[0] == "y":
            for file in needs_to_update:
                update_file(owner, repo, file)
            print("All files updated.")
            with open(os.environ["LOG_FILE"], "a") as f:
                print("All files updated.", file=f)
        else:
            print("File updates suppressed.")
            with open(os.environ["LOG_FILE"], "a") as f:
                print("File updates suppressed.", file=f)
    else:
        print("All files are up to date.")
        with open(os.environ["LOG_FILE"], "a") as f:
            print("All files are up to date.", file=f)

def check_all(owner, repo):
    for file in FILES:
        if not compare_files(owner, repo, file):
            return False

def exists(owner, repo, path, branch='main', token=None):
    return misc.get_github_file_content(owner, repo, path, branch, token) is not None