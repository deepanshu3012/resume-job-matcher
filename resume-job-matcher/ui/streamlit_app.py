import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parser.resume_parser import extract_text_from_pdf
from utils.matcher import compute_similarity


st.set_page_config(page_title="🧠 Resume-Job Matcher", layout="wide")

st.title("🧠 Resume and Job Matcher")

st.header("1️⃣ Upload Resume")
uploaded_resume = st.file_uploader("Upload your resume (PDF)", type=['pdf'])

st.header("2️⃣ Enter Job Description")
job_description = st.text_area("Paste the job description here")

if st.button("Match Resume to Job Description"):
    if uploaded_resume and job_description:
        resume_text = extract_text_from_pdf(uploaded_resume)
        score = compute_similarity(resume_text, job_description)
        st.success(f"✅ Similarity Score: {score}")
    else:
        st.error("Please upload a resume and enter a job description.")
