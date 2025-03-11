import misc
import os
import platform

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
        if not compare_files("EclipseShadow55", "Twitch-Connector", file):
            needs_to_update.append(file)
            update = True
    print("Update needed, updating..." if update else "No update needed, returning to main program.")
    with open(os.environ["LOG_FILE"], "a") as f:
        print("Update needed, updating..." if update else "No update needed, returning to main program.", file=f)
    if update:
        for file in needs_to_update:
            update_file(owner, repo, file)
        if platform.system() == "Windows":
            os.system(f"python {os.path.dirname(os.path.abspath(__file__))}\main.pyw")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system(f"python3 {os.path.dirname(os.path.abspath(__file__))}\main.pyw")
        else:
            raise OSError(f"Unsupported OS: {platform.system()}")
        print("\n")
        with open(os.environ["LOG_FILE"], "a") as f:
            print("\n", file=f)
        exit(0)

def exists(owner, repo, path, branch='main', token=None):
    return misc.get_github_file_content(owner, repo, path, branch, token) is not None