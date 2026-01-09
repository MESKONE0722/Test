# Test
# Rhode Island DOC Written Test - Practice Exam

An interactive web application for practicing the Rhode Island Department of Corrections written examination.

## Features

- 50 practice questions covering all test sections
- Real-time progress tracking
- Automatic scoring with pass/fail indicator
- Detailed results breakdown by section
- Review incorrect answers
- Mobile-friendly interface

## Test Sections

1. Reading Comprehension
1. Written Expression & Grammar
1. Mathematics
1. Situational Judgment
1. Policy Application & Reasoning
1. Memory & Observation
1. Ethics & Professional Conduct

## Passing Requirements

- **Total Questions:** 50
- **Passing Score:** 35 correct answers (70%)
- **Time Limit:** 90 minutes (not enforced in practice mode)

## How to Run Locally

1. Clone this repository:

```bash
git clone <your-repo-url>
cd <repo-name>
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Run the app:

```bash
streamlit run ri_doc_test_app.py
```

1. Open your browser to the URL shown (usually http://localhost:8501)

## Deploy to Streamlit Cloud

1. Push this repo to GitHub (can be public or private)
1. Go to https://share.streamlit.io/
1. Sign in with GitHub
1. Click “New app”
1. Select your repository, branch, and main file (ri_doc_test_app.py)
1. Click “Deploy”

Your app will be live at a public URL like: `https://your-app-name.streamlit.app`

## Files in This Repo

- `ri_doc_test_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Disclaimer

This is a sample practice test for preparation purposes only. Actual Rhode Island DOC examinations may vary in format, content, and difficulty. Candidates should consult official RIDOC resources for current testing requirements.

## License

For educational and practice purposes only.
