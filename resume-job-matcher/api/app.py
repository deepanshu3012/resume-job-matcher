import streamlit as st
from parser.resume_parser import parse_resume
from parser.job_parser import parse_job_description
from matcher.match_engine import match_scores
import os

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 Resume to Job Matcher")

# Upload resume
resume_file = st.file_uploader("Upload Resume (.txt only)", type=['txt'])

# Select job description file
job_files = os.listdir("data/job_descriptions")
selected_job = st.selectbox("Select a Job Description", job_files)

if st.button("Match"):
    if resume_file and selected_job:
        # Save uploaded resume temporarily
        with open("temp_resume.txt", "wb") as f:
            f.write(resume_file.read())

        resume_data = parse_resume("temp_resume.txt")
        job_data = parse_job_description(f"data/job_descriptions/{selected_job}")
        result = match_scores(resume_data, job_data)

        st.markdown(f"### 👤 Candidate: {resume_data['name']}")
        st.markdown(f"📧 Email: {resume_data['contact']['email']}")
        st.markdown(f"📞 Phone: {resume_data['contact']['phone']}")
        st.markdown(f"### ✅ Matching Score: {result['score']}%")
        st.markdown(f"### 🧠 Matched Skills:")
        st.write(result['matched_skills'])
    else:
        st.error("Please upload a resume and select a job description.")
