import subprocess

def start_hadoop():
    command = 'su - hadoop -c "/usr/local/hadoop/sbin/start-dfs.sh"'
    result = subprocess.run(["wsl", command], capture_output=True, text=True)

    command = 'su - hadoop -c "/usr/local/hadoop/sbin/start-yarn.sh"'
    result = subprocess.run(["wsl", command], capture_output=True, text=True)


    #subprocess.run(["wsl", "su", "-", "hadoop", "-c", "/usr/local/hadoop/sbin/start-dfs.sh"])
    #subprocess.run(["wsl", "su", "-", "hadoop", "-c", "source ~/.bashrc && start-yarn.sh"])

if __name__ == "__main__":
    start_hadoop()
