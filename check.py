import subprocess

def temp():
    return subprocess.run(["watch", "-n", "2", "sensors"])