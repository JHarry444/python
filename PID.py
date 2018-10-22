import subprocess

res = subprocess.check_output(["ps -ax", "|", "cut -d  -f1"])