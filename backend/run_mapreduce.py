import subprocess

def run_mapreduce():
    print("Starting MapReduce job...")

    jar_path = '/home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar'
    # It's a Java archive (.jar) that allows you to run MapReduce jobs using scripts (like Python, not just Java)
    # Hadoop uses this JAR to run your Python mapper.py and reducer.py as part of the MapReduce job.
    # It is the tool that connects your Python code to Hadoop’s MapReduce engine.

    # Remove output directory if it already exists
    subprocess.run([
        "wsl", "bash", "-c", 
        "sudo -u hadoop /home/hadoop/hadoop-3.3.6/bin/hdfs dfs -rm -r /resume_output"
    ], stderr=subprocess.DEVNULL)

    # Run MapReduce job using Hadoop Streaming inside WSL
    # Hadoop Streaming is a utility that lets you write MapReduce programs in any language (like Python, not just Java)
    mapreduce_command = (
        'sudo -u hadoop bash -c "/home/hadoop/hadoop-3.3.6/bin/hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar  '
        '-input /resume_project/input/text_resumes '
        '-output /resume_output '
        '-mapper \\"python3 mapper.py\\" '
        '-reducer \\"python3 reducer.py\\" '
        '-file /mnt/e/HadoopScripts/ResumeAnalyzer/mapper.py '
        '-file /mnt/e/HadoopScripts/ResumeAnalyzer/reducer.py"'
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
