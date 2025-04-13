# backend/utils.py
import subprocess

def run_in_wsl(command):
    full_cmd = f"wsl bash -c '{command}'"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    if result.stderr:
        print("Error:", result.stderr)
    return result.stdout.strip()
