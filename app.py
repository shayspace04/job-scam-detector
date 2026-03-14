import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Fake Internship / Job Scam Detector")

st.write("Paste a job description to check if it might be a scam.")

job_text = st.text_area("Job Description")

if st.button("Analyze Job"):

    if job_text.strip() == "":
        st.warning("Please paste a job description.")
    else:

        vec = vectorizer.transform([job_text])

        prediction = model.predict(vec)[0]
        probability = model.predict_proba(vec)[0][1]

        risk_score = round(probability * 100, 2)

        st.subheader(f"Fraud Risk Score: {risk_score}%")

        if prediction == 1:
            st.error("⚠️ This job posting may be a SCAM.")
            suspicious_keywords = [
                           "earn money fast",
                           "work from home",
                           "whatsapp",
                           "no experience",
                           "quick money",
                           "investment required"
            ]

            found = [word for word in suspicious_keywords if word in job_text.lower()]

            if found:
                st.warning("⚠️ Suspicious phrases detected:")
                for word in found:
                   st.write(f"- {word}")
        else:
            st.success("✅ This job posting appears LEGITIMATE.")