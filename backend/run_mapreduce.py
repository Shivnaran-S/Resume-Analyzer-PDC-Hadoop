import subprocess

def run_mapreduce():
    print("Starting MapReduce job...")

    jar_path = '/home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar'

    # Remove output directory if it already exists
    subprocess.run([
        "wsl", "bash", "-c", 
        "sudo -u hadoop hdfs dfs -rm -r /resume_output"
    ], stderr=subprocess.DEVNULL)

    # Run MapReduce job
    mapreduce_command = (
        'sudo -u hadoop bash -c "hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar  '
        '-input /resume_data '
        '-output /resume_output '
        '-mapper mapper.py '
        '-reducer reducer.py '
        '-file backend/mapper.py '
        '-file backend/reducer.py"'
    )

    result = subprocess.run(
        ["wsl", "bash", "-c", mapreduce_command],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("MapReduce job completed successfully!")
    else:
        print("MapReduce job failed!")
        print(result.stderr)

if __name__ == "__main__":
    run_mapreduce()
