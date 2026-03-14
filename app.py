import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("🕵️ Fake Internship / Job Scam Detector")

st.write("Paste a job description to check if it might be a scam.")

job_text = st.text_area("Job Description")

if st.button("Analyze Job"):

    if job_text.strip() == "":
        st.warning("Please enter a job description.")

    else:

        # ML Prediction
        text_vec = vectorizer.transform([job_text])
        probability = model.predict_proba(text_vec)[0][1]

        risk_score = probability * 100

        # Suspicious phrases
        suspicious_keywords = [
            "work from home",
            "earn money fast",
            "whatsapp",
            "telegram",
            "no experience",
            "quick money",
            "investment required",
            "easy money",
            "daily income",
            "registration fee",
            "limited slots"
        ]

        found_keywords = [
            word for word in suspicious_keywords if word in job_text.lower()
        ]

        # Detect unrealistic salary
        numbers = re.findall(r'\d+', job_text)
        salary_flag = any(int(n) > 1000000 for n in numbers)

        # Adjust risk score
        if salary_flag:
            risk_score += 25

        if found_keywords:
            risk_score += 20

        risk_score = min(risk_score, 100)

        # Show score
        st.subheader(f"Fraud Risk Score: {risk_score:.2f}%")

        # Decision
        if risk_score > 60:
            st.error("⚠ High probability of JOB SCAM")

        elif risk_score > 35:
            st.warning("⚠ Potentially suspicious job posting")

        else:
            st.success("✅ This job posting appears relatively legitimate")

        # Explain suspicious elements
        if found_keywords:
            st.warning("⚠ Suspicious phrases detected:")
            for word in found_keywords:
                st.write(f"- {word}")

        if salary_flag:
            st.warning("⚠ Unrealistically high salary detected")

        # AI Explanation Section
        explanation = []

        if found_keywords:
            explanation.append(
                "The job description contains phrases commonly used in fraudulent job postings."
            )

        if salary_flag:
            explanation.append(
                "The salary mentioned appears unusually high and may indicate a potential scam."
            )

        if risk_score > 60:
            explanation.append(
                "Overall analysis suggests a high likelihood that the job posting may be fraudulent."
            )

        elif risk_score > 35:
            explanation.append(
                "The posting shows some suspicious indicators and should be evaluated carefully."
            )

        else:
            explanation.append(
                "No strong scam indicators were detected, though users should always verify job authenticity."
            )

        st.subheader("AI Explanation")

        for line in explanation:
            st.write(line)
