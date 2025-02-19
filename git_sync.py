import subprocess

def git_sync(commit_message="Auto-commit"):
    """Sync local changes to the current Git branch."""
    try:
        # Get the current branch name
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")

        # Check if there are any changes to commit
        status = subprocess.check_output(["git", "status", "--porcelain"]).strip().decode("utf-8")

        if status:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to remote (even if there were no new commits)
        subprocess.run(["git", "push", "origin", branch], check=True)

        print(f"✅ Synced to Git branch: {branch}")
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Git sync failed: {e}")

if __name__ == "__main__":
    import sys
    message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Auto-commit"
    git_sync(message)




# run this command in the terminal "python git_sync.py "your commit message""