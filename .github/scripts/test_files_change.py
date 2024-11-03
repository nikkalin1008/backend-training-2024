import subprocess
import re
import sys

# Color settings
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
GREEN = '\033[0;32m'
NC = '\033[0m'  # No Color

def run_command(command):
    """Helper function to run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def main():
    try:
        # Check if there is a parent commit (to avoid errors on the first commit)
        parent_commit_exists = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD^"],
            capture_output=True,
            text=True
        ).returncode == 0

        if parent_commit_exists:
            # If there is a parent commit, perform a diff comparison
            modified_files = run_command("git diff --name-only HEAD^ HEAD")
        else:
            # If this is the first commit, list the files in the current commit
            modified_files = run_command("git ls-tree --name-only -r HEAD")

        print("Modified files:")
        print(modified_files)

        # Filter out files outside the 'members/' directory, while ignoring the '.gitmodules' file
        non_member_files = [
            f for f in modified_files.splitlines()
            if not re.match(r'^members/|^\.gitmodules$', f)
        ]

        if non_member_files:
            print(f"{RED}Error: The following non-members/ files were modified (excluding .gitmodules):{NC}", file=sys.stderr)
            print(f"{YELLOW}{'\n'.join(non_member_files)}{NC}", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"{GREEN}Only members/ directory or .gitmodules was modified. Proceeding...{NC}")

    except Exception as e:
        print(f"{RED}An error occurred: {e}{NC}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
