# 🧠 Resume-Job Matcher (Streamlit App)

This project is an intelligent Resume-Job Matcher built using Python and Streamlit. It allows users to **upload a resume (PDF)** and **select a job description** (manually or by uploading) to find the best match between the candidate's skills and the job's requirements — all without needing preloaded datasets.

---

## 🚀 Features

- ✅ Upload Resume (PDF format)
- ✅ Manually paste or upload Job Description
- ✅ NLP-based keyword matching and similarity scoring
- ✅ Simple and interactive UI with Streamlit
- ✅ No need for preloaded datasets

---

## 📦 Requirements

Make sure Python 3.8+ is installed. Install the dependencies using:

```bash
pip install -r requirements.txt
# resume-job-matcher
💻 How to Run
bash
streamlit run ui/streamlit_app.py
This will open a web interface in your browser at http://localhost:8501.

📁 Folder Structure
resume-job-matcher/
│
├── api/                    # API logic (optional)
├── matcher/                # Matching engine logic
├── parser/                 # Resume and job description parsing
│   ├── resume_parser.py
│   └── job_parser.py
├── ui/
│   └── streamlit_app.py    # Main Streamlit app
├── requirements.txt
├── .gitignore
└── README.md

📚 Usage
Run the app.

Upload a resume in PDF format.

Either paste a job description or upload a .txt/.pdf file.

See the match results and similarity score!

🧠 Tech Stack
Python 🐍

Streamlit 🎈

spaCy / NLTK for NLP

Scikit-learn (TfidfVectorizer or similar)

PDFMiner or PyMuPDF for reading PDFs

🛡️ License
MIT License. Feel free to use, modify, and share this project!

👨‍💻 Author
Deepanshu Joshi
GitHub: deepanshu3012


