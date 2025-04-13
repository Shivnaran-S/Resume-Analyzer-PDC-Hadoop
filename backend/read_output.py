# backend/read_output.py
from .utils import run_in_wsl

def fetch_output():
    output_hdfs_dir = "/resume_project/output/part-r-00000"
    local_output = "/mnt/e/Siva Naran/Sem 6/PDC/Package/Resume Analyzer PDC Hadoop/output/hadoop_output.txt"

    # Get output from HDFS to local file
    run_in_wsl(f"hdfs dfs -get -f {output_hdfs_dir} {local_output}")
