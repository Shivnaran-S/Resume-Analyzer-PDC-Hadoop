# backend/hdfs_uploader.py
from .utils import run_in_wsl
import os

def upload_to_hdfs():
    hdfs_input_dir = "/resume_project/input"
    local_text_dir = "/mnt/e/Siva\\ Naran/Sem\\ 6/PDC/Package/Resume\\ Analyzer\\ PDC\\ Hadoop/data/text_resumes"

    print("Creating HDFS input directory...")
    run_in_wsl(f"/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -mkdir -p {hdfs_input_dir}")

    print(f"Uploading files from {local_text_dir} to HDFS...")
    inner_command = f'cd {local_text_dir} && /home/hadoop/hadoop-3.3.6/bin/hdfs dfs -put . {hdfs_input_dir}'
    wrapped_command = f'bash -c "{inner_command}"'
    run_in_wsl(wrapped_command)

    print("Upload Complete")
if __name__=="__main__":
    upload_to_hdfs()