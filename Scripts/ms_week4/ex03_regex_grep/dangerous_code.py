import subprocess
import os

def safe_command():
    # Safe: list form, no shell
    subprocess.Popen(["ls", "-la"])

def dangerous_command():
    # DANGEROUS: shell=True with string interpolation
    filename = "report.txt"
    subprocess.Popen(f"cat {filename}", shell=True)

def another_dangerous():
    # DANGEROUS: shell=True
    user_input = "somefile"
    subprocess.Popen("grep pattern " + user_input, shell=True)

def also_safe():
    subprocess.run(["echo", "hello"], capture_output=True)
