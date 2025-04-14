import subprocess

def start_hadoop():
    #subprocess.run(["wsl", "su", "-", "hadoop", "-c", "/home/hadoop/hadoop-3.3.6/sbin/start-dfs.sh"])
    #subprocess.run(["wsl", "su", "-", "hadoop", "-c", "/home/hadoop/hadoop-3.3.6/sbin/stop-yarn.sh"])
    subprocess.run(["wsl", "bash", "-c", "sudo -u hadoop /home/hadoop/hadoop-3.3.6/sbin/start-dfs.sh"])
    #subprocess.run(["wsl", "bash", "-c", "sudo -u hadoop /home/hadoop/hadoop-3.3.6/sbin/stop-yarn.sh"])


if __name__ == "__main__":
    start_hadoop()
