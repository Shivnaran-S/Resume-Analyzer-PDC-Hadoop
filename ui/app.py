import streamlit as st
import os
import subprocess

st.title("📄 Resume Uploader")

# ✅ Automatically start Hadoop services
'''
with st.spinner("🚀 Starting Hadoop services..."):
    subprocess.run(["wsl", "bash", "-c", "sudo -u hadoop /home/hadoop/hadoop-3.3.6/sbin/start-dfs.sh"])
    subprocess.run(["wsl", "bash", "-c", "sudo -u hadoop /home/hadoop/hadoop-3.3.6/sbin/start-yarn.sh"])
'''

uploaded_files = st.file_uploader("Upload PDF Resumes", type="pdf", accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data/resumes", exist_ok=True)
    for file in uploaded_files:
        with open(f"data/resumes/{file.name}", "wb") as f:
            f.write(file.read())
    st.success(f"{len(uploaded_files)} resume(s) uploaded successfully!")

    if st.button("🔁 Process Resumes"):
        os.system("python backend/text_converter.py")
        os.system("python -m backend.hdfs_uploader")
        os.system("python backend/run_mapreduce.py")
        os.system("python -m backend.read_output")
        '''
        with open("output/hadoop_output.txt") as f:
            output = f.read()
            st.subheader("Top Skills Found 📊")
            st.text(output)

        '''
        