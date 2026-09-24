import subprocess

def run_backup(user_input):
    # Intentional issue: shell injection via unsanitized input
    subprocess.run("tar -czf /tmp/backup.tar.gz " + user_input, shell=True)

def divide(a, b):
    # Intentional issue: no handling for b == 0
    return a / b
