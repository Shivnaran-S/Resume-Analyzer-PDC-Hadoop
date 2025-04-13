# backend/hdfs_uploader.py
from .utils import run_in_wsl
import os

def upload_to_hdfs():
    hdfs_input_dir = "/resume_project/input"
    local_text_dir = "/mnt/e/Siva Naran/Sem 6/PDC/Package/Resume Analyzer PDC Hadoop/data/text_resumes"

    # 1. Create HDFS directory
    run_in_wsl(f"hdfs dfs -mkdir -p {hdfs_input_dir}")

    # 2. Upload all .txt files from text_resumes/
    run_in_wsl(f"hdfs dfs -put -f {local_text_dir}/*.txt {hdfs_input_dir}")
