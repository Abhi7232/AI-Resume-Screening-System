# 📄 AI Resume Screening & Candidate Ranking System

An AI-powered recruitment automation system that analyzes resumes, extracts candidate information, matches resumes with job descriptions, and ranks candidates using Artificial Intelligence, Natural Language Processing (NLP), and Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Machine Learning](https://img.shields.io/badge/AI-Machine%20Learning-green)
![NLP](https://img.shields.io/badge/NLP-Enabled-orange)

---

# 📌 Project Overview

Recruitment teams often need to analyze a large number of resumes manually, which is a time-consuming and inefficient process.

To solve this problem, I developed an **AI Resume Screening & Candidate Ranking System** that automates the initial candidate screening process using Artificial Intelligence, Natural Language Processing (NLP), and Machine Learning techniques.

The system analyzes PDF resumes, extracts important candidate information, identifies technical skills, calculates resume scores, matches candidates with job descriptions, and ranks candidates based on their overall compatibility score.

This project helps recruiters save time, improve candidate selection, and quickly identify the most suitable candidates for a job role.

---

# ✨ Features

## 📄 Resume Upload & Parsing
- Upload multiple resumes in PDF format.
- Extract resume text automatically.
- Extract candidate details like:
  - Name
  - Email
  - Phone
  - Education
  - Experience

## 🎯 Skill Detection
- Automatically identifies technical skills from resumes.
- Supports skills like:
  - Python
  - SQL
  - Pandas
  - NumPy
  - Machine Learning
  - Deep Learning
  - TensorFlow
  - PyTorch
  - Streamlit
  - Git
  - GitHub

## 📊 Resume Scoring System
- Calculates candidate resume score based on detected skills.
- Evaluates candidate profile strength.

## 🔍 Job Description Matching
- Compares resumes with job descriptions.
- Calculates candidate compatibility percentage using NLP-based matching.

## 🏆 Candidate Ranking
- Ranks candidates based on combined score:

  - 50% Resume Score
  - 50% Job Description Match

## 🤖 AI Candidate Prediction
Predicts candidate status:

- Selected
- Shortlisted
- Rejected

## 📈 Analytics Dashboard
- Displays candidate statistics.
- Shows score distribution.
- Provides selection insights.

## ❓ Interview Questions Generator
- Provides technical interview questions for candidates.

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Framework
- Streamlit

## Artificial Intelligence & Machine Learning
- Natural Language Processing (NLP)
- Machine Learning
- Scikit-learn

## Data Processing & Visualization
- Pandas
- NumPy
- Matplotlib

## Resume Processing
- PDF Text Extraction
- Resume Parsing
- Skill Extraction

## Development Tools
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```
AI_Resume_Screening_System

│── app.py
│── requirements.txt
│── README.md
│
└── utils
    │── pdf_parser.py
    │── resume_parser.py
    │── matcher.py
    │── predictor.py
    │── summary.py
    │── experience_parser.py
    │── education_parser.py
```

---

# ⚙️ Installation & How to Run

Follow these steps to run the project on your local system.

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## 2. Navigate to Project Folder

```bash
cd AI_Resume_Screening_System
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser and you can start uploading PDF resumes.

---

# 🔄 Project Workflow

```
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Extract Candidate Details
(Name, Email, Phone, Education, Experience)
        ↓
Detect Technical Skills
        ↓
Calculate Resume Score
        ↓
Match Resume With Job Description
        ↓
Generate Final Candidate Score
        ↓
Rank Candidates
        ↓
AI Prediction
```

---

# 📊 Scoring System

Candidate ranking is calculated using:

```
Final Score = 50% Resume Score + 50% Job Description Match
```

Example:

```
Resume Score = 80%

Job Match = 70%

Final Score = 75%
```

---

# 🚀 Future Improvements

- Database Integration
- User Authentication
- Advanced NLP Models
- BERT / Transformer-based Matching
- Cloud Deployment
- Real-time Recruitment Dashboard

---

# 👨‍💻 Author

**Abhishek Kanojiya**

B.Tech Computer Science Engineering & Artificial Intelligence

---

⭐ If you like this project, consider giving it a star on GitHub.