import streamlit as st
import os
import subprocess

st.title("📄 Resume Uploader")

# ✅ Automatically start Hadoop services
with st.spinner("🚀 Starting Hadoop services..."):
    command = 'su - hadoop -c "/usr/local/hadoop/sbin/start-dfs.sh"'
    result = subprocess.run(["wsl", command], capture_output=True, text=True)

    command = 'su - hadoop -c "/usr/local/hadoop/sbin/start-yarn.sh"'
    result = subprocess.run(["wsl", command], capture_output=True, text=True)

uploaded_files = st.file_uploader("Upload PDF Resumes", type="pdf", accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data/resumes", exist_ok=True)
    for file in uploaded_files:
        with open(f"data/resumes/{file.name}", "wb") as f:
            f.write(file.read())
    st.success(f"{len(uploaded_files)} resume(s) uploaded successfully!")

    if st.button("🔁 Process Resumes"):
        os.system("python backend/text_converter.py")
        os.system("python backend/hdfs_uploader.py")
        os.system("python backend/run_mapreduce.py")
        os.system("python backend/read_output.py")

        with open("output/hadoop_output.txt") as f:
            output = f.read()
            st.subheader("Top Skills Found 📊")
            st.text(output)
