import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.pdf_parser import extract_text_from_pdf
from utils.resume_parser import (
    extract_name,
    extract_email,
    extract_phone
)
from utils.matcher import calculate_similarity
from utils.experience_parser import extract_experience
from utils.education_parser import extract_education
from utils.summary import generate_summary
from utils.predictor import predict_candidate
# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

if "candidates" not in st.session_state:
    st.session_state.candidates = []

# ----------------------------------------
# Title
# ----------------------------------------

st.title("📄 AI Resume Screening & Candidate Ranking System")

st.markdown(
    """
    Upload resumes and screen candidates using Artificial Intelligence.
    """
)

st.divider()

# ----------------------------------------
# Sidebar
# ----------------------------------------

st.sidebar.title("🤖 AI Resume Screening")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📄 Upload Resume",
        "📊 Candidate Ranking",
        "🤖 AI Prediction",
        "❓ Interview Questions",
        "📈 Analytics"
    ]
)

# ----------------------------------------
# Home Page
# ----------------------------------------

if page == "🏠 Home":

    st.header("🏠 Welcome")

    st.success("AI Resume Screening System is Running Successfully ✅")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("PDF Upload", "Enabled")

    with col2:
        st.metric("Resume Parser", "Ready")

    with col3:
        st.metric("AI Status", "Active")

    st.divider()

    st.subheader("✨ Features")

    st.write("✅ Upload Resume")
    st.write("✅ Extract Candidate Details")
    st.write("✅ Skill Detection")
    st.write("✅ Resume Score")
    st.write("✅ Job Description Matching")
    st.write("✅ Candidate Ranking")

# ----------------------------------------
# Upload Resume
# ----------------------------------------

elif page == "📄 Upload Resume":

    st.header("📄 Upload Resume")

    uploaded_files = st.file_uploader(
        "Upload Resume(s) (PDF)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        skills = [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Streamlit",
            "Git",
            "GitHub",
            "Flask",
            "Django",
            "Power BI",
            "Excel",
            "XGBoost",
            "Random Forest"
        ]

        for uploaded_file in uploaded_files:

            st.divider()
            st.subheader(f"📄 {uploaded_file.name}")

            resume_text = extract_text_from_pdf(uploaded_file)

            name = extract_name(resume_text)
            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            experience = extract_experience(resume_text)
            education = extract_education(resume_text)

            st.success("Resume Uploaded Successfully ✅")

            st.subheader("📄 Resume Text")

            st.text_area(
                f"Extracted Resume - {uploaded_file.name}",
                resume_text,
                height=250,
                key=f"text_{uploaded_file.name}"
            )

            col1, col2 = st.columns(2)
            with col1:
                st.write("### 👤 Name")
                st.success(name)

                st.write("### 📧 Email")
                st.success(email)

            with col2:
                st.write("### 📱 Phone")
                st.success(phone)

                st.write("### 💼 Experience")
                st.success(experience)

                st.write("### 🎓 Education")
                st.success(education)

            # -----------------------------
            # Skill Detection
            # -----------------------------

            detected_skills = []

            for skill in skills:
                if skill.lower() in resume_text.lower():
                    detected_skills.append(skill)

            st.write("### 🎯 Skills")

            if detected_skills:
                st.success(", ".join(detected_skills))
            else:
                st.error("No Skills Found")

            # -----------------------------
            # AI Resume Summary
            # -----------------------------

            summary = generate_summary(
                name,
                education,
                experience,
                ", ".join(detected_skills)
            )

            st.subheader("📝 AI Resume Summary")
            st.info(summary)

            # -----------------------------
            # Resume Score
            # -----------------------------

            total_skills = len(skills)
            detected_count = len(detected_skills)

            score = int((detected_count / total_skills) * 100)

            st.metric("Resume Score", f"{score}%")
            st.progress(score / 100)

            if score >= 80:
                st.success("🟢 Recommended")
            elif score >= 60:
                st.warning("🟡 Shortlist for Interview")
            else:
                st.error("🔴 Not Recommended")

            # -----------------------------
            # Save Candidate
            # -----------------------------

            candidate_data = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Education": education,
                "Score": score,
                "Resume Score": score,
                "Match %": 0.0,
                "Skills": ", ".join(detected_skills)
            }

            st.session_state.candidates = [
                c for c in st.session_state.candidates
                if c["Email"] != email
            ]

            st.session_state.candidates.append(candidate_data)

        st.divider()

        st.subheader("📄 Job Description Matching")

        job_description = st.text_area(
            "Paste Job Description",
            height=200
        )

        if st.button("🔍 Match Resume"):

            if job_description.strip() == "":
                st.warning("Please enter Job Description.")

            else:
                for c in st.session_state.candidates:

                    similarity = calculate_similarity(
                        c["Skills"] + " " + c["Education"] + " " + c["Experience"],
                        job_description
                    )

                    similarity = float(similarity)

                    c["Match %"] = similarity

                    final_score = int(
                        (c["Resume Score"] * 0.5) +
                        (similarity * 0.5)
                    )

                    c["Score"] = final_score

                st.success("✅ All resumes matched with Job Description successfully.")
# ----------------------------------------
# Candidate Ranking
# ----------------------------------------

elif page == "📊 Candidate Ranking":

    st.header("📊 Candidate Ranking")

    if len(st.session_state.candidates) > 0:

        ranking = sorted(
            st.session_state.candidates,
            key=lambda x: x["Score"],
            reverse=True
        )

        # Search Candidate
        search = st.text_input("🔍 Search Candidate by Name")

        if search:
            ranking = [
                c for c in ranking
                if search.lower() in c["Name"].lower()
            ]

        # Minimum Score Filter
        min_score = st.slider(
            "Minimum Resume Score",
            0,
            100,
            0
        )

        ranking = [
            c for c in ranking
            if c["Score"] >= min_score
        ]

        df = pd.DataFrame(ranking)

        if not df.empty:

            df = df[
                [
                    "Name",
                    "Score",
                    "Resume Score",
                    "Match %",
                    "Experience",
                    "Education",
                    "Skills"
                ]
            ]
            df.index = range(1, len(df) + 1)
            df.index.name = "Rank"

            st.dataframe(
                df,
                use_container_width=True
            )

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Candidate Ranking",
                data=csv,
                file_name="candidate_ranking.csv",
                mime="text/csv"
            )

            st.subheader("🏆 Top Candidates")

            for i, candidate in enumerate(ranking, start=1):

                if i == 1:
                    medal = "🥇"
                elif i == 2:
                    medal = "🥈"
                elif i == 3:
                    medal = "🥉"
                else:
                    medal = "🏅"

                st.write(f"""
{medal} Rank {i}

**Name:** {candidate["Name"]}

**Score:** {candidate["Score"]}%

**Match:** {candidate["Match %"]:.2f}%

**Experience:** {candidate["Experience"]}

**Education:** {candidate["Education"]}

**Skills:** {candidate["Skills"]}
""")

                st.divider()

        else:
            st.warning("No candidate matches the selected filters.")

    else:
        st.info("No candidates uploaded yet.")
# ----------------------------------------
# AI Prediction
# ----------------------------------------

elif page == "🤖 AI Prediction":

    st.header("🤖 AI Candidate Prediction")

    if len(st.session_state.candidates) == 0:
        st.info("Please upload at least one resume.")

    else:

        names = [c["Name"] for c in st.session_state.candidates]

        selected_name = st.selectbox(
            "Select Candidate",
            names
        )

        candidate = next(
            c for c in st.session_state.candidates
            if c["Name"] == selected_name
        )

        st.subheader("👤 Candidate Details")

        st.write(f"**Name:** {candidate['Name']}")

        st.write(f"**Final Score:** {candidate['Score']}%")

        st.write(f"**Resume Score:** {candidate['Resume Score']}%")

        st.write(f"**Job Match:** {candidate['Match %']:.2f}%")

        st.write(f"**Experience:** {candidate['Experience']}")

        st.write(f"**Education:** {candidate['Education']}")

        st.write(f"**Skills:** {candidate['Skills']}")

        st.divider()

        score = candidate["Score"]
        match = candidate["Match %"]

        prediction = predict_candidate(score, match)

        if prediction == "Selected":
            st.success("✅ Prediction : Selected")
            st.balloons()

        elif prediction == "Shortlisted":
            st.warning("🟡 Prediction : Shortlisted")

        else:
            st.error("❌ Prediction : Rejected")

        st.subheader("📋 AI Decision")

        if prediction == "Selected":
            st.info(
                "Candidate has a strong resume and an excellent job match."
            )

        elif prediction == "Shortlisted":
            st.info(
                "Candidate should be considered for the interview."
            )

        else:
            st.info(
                "Candidate does not meet the required criteria."
            )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Resume Score", f"{score}%")
            st.progress(score / 100)

        with col2:
            st.metric("Job Match", f"{match:.2f}%")
            st.progress(match / 100)

        st.subheader("🤖 Machine Learning Prediction")

        result_color = {
            "Selected": "🟢",
            "Shortlisted": "🟡",
            "Rejected": "🔴"
        }

        st.success(
            f"{result_color[prediction]} Final ML Prediction: {prediction}"
        )
# ----------------------------------------
# Interview Questions
# ----------------------------------------

elif page == "❓ Interview Questions":

    st.header("❓ AI Interview Questions")

    questions = [
        "Explain the difference between Supervised and Unsupervised Learning.",
        "What is Overfitting?",
        "What is Random Forest?",
        "Difference between Pandas and NumPy?",
        "Explain Logistic Regression.",
        "What is XGBoost?",
        "Difference between Classification and Regression?",
        "What is Cross Validation?",
        "What is Streamlit?",
        "Tell me about yourself."
    ]

    for i, q in enumerate(questions, start=1):
        st.write(f"{i}. {q}")

# ----------------------------------------
# Analytics
# ----------------------------------------

elif page == "📈 Analytics":

    st.header("📈 Analytics Dashboard")

    total = len(st.session_state.candidates)

    st.metric("Total Candidates", total)

    if total > 0:

        scores = [c["Score"] for c in st.session_state.candidates]

        st.metric(
            "Highest Score",
            max(scores)
        )

        st.metric(
            "Average Score",
            round(sum(scores) / total, 2)
        )

        st.divider()

        st.subheader("📊 Candidate Selection Status")

        selected = len([
            c for c in st.session_state.candidates
            if c["Score"] >= 80
        ])

        shortlisted = len([
            c for c in st.session_state.candidates
            if 60 <= c["Score"] < 80
        ])

        rejected = len([
            c for c in st.session_state.candidates
            if c["Score"] < 60
        ])

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.pie(
            [selected, shortlisted, rejected],
            labels=["Selected", "Shortlisted", "Rejected"],
            autopct="%1.1f%%",
            startangle=90
        )

        ax.axis("equal")

        st.pyplot(fig)

        st.divider()

        chart_data = pd.DataFrame({
            "Candidate": [c["Name"] for c in st.session_state.candidates],
            "Score": [c["Score"] for c in st.session_state.candidates]
        })

        st.subheader("📊 Score Distribution")

        st.bar_chart(
            chart_data.set_index("Candidate")
        )

    else:
        st.info("No candidates available.")