# backend/read_output.py
from .utils import run_in_wsl

def fetch_output():
    hdfs_output = "/resume_output/part-00000"
    linux_dir = "/home/hadoop/temp_output"
    linux_output = f"{linux_dir}/hadoop_output.txt"
    windows_output = "/mnt/e/Siva\\ Naran/Sem\\ 6/PDC/Package/Resume\\ Analyzer\\ PDC\\ Hadoop/output/"

    # Ensure the target WSL directory exists
    run_in_wsl(f"mkdir -p {linux_dir}")

    # Download file to WSL native directory
    run_in_wsl(f"/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -get -f {hdfs_output} {linux_output}")

    # Copy file from WSL to Windows path
    run_in_wsl(f"cp {linux_output} {windows_output}")

if __name__ == "__main__":
    fetch_output()
