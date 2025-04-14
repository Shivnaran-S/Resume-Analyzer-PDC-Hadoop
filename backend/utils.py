# backend/utils.py
import subprocess

def run_in_wsl(command):
    #command = command.replace("hdfs", "/home/hadoop/hadoop-3.3.6/bin/hdfs")
    #ommand = command.replace("hadoop", "/home/hadoop/hadoop-3.3.6/bin/hadoop")
    
    full_cmd = f"wsl bash -c 'sudo -u hadoop {command}'"
    #print(full_cmd)
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    # ✅ Print both stdout and stderr
    if result.stdout:
        print("✅ Output:\n", result.stdout)
    if result.stderr:
        print("⚠️ Error:\n", result.stderr)
    return result.stdout.strip()
