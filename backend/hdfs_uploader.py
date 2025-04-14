# backend/hdfs_uploader.py
from .utils import run_in_wsl
import os

def upload_to_hdfs():
    hdfs_input_dir = "/resume_project/input"
    local_text_dir = "/mnt/e/Siva Naran/Sem 6/PDC/Package/Resume Analyzer PDC Hadoop/data/text_resumes"

    # 1. Create HDFS directory
    #print("📁 Creating HDFS input directory...")
    #run_in_wsl(f"/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -mkdir -p {hdfs_input_dir}")

    # 2. Upload all .txt files from text_resumes/
    print(f"📤 Uploading files from {local_text_dir} to HDFS...")
    run_in_wsl(f'/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -put -f "{local_text_dir}" "{hdfs_input_dir}"')
    #run_in_wsl(f"/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -put -f \"{local_text_dir}\"/* \"{hdfs_input_dir}\"")
    #run_in_wsl(f'/home/hadoop/hadoop-3.3.6/bin/hdfs dfs -put -f "{local_text_dir}"/* "{hdfs_input_dir}"')

    #print("✅ Upload complete.")

if __name__=="__main__":
    upload_to_hdfs()