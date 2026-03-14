# Fake internship-job-scam-detector
Machine Learning project that detects potentially fraudulent job postings using NLP and Random Forest classification.

As a student actively applying for internships and jobs, I often came across opportunities that seemed suspicious — especially “work from home” roles promising unrealistic salaries or asking candidates to contact recruiters through personal messaging platforms.
This project was built to explore whether machine learning and natural language processing (NLP) could help identify patterns commonly found in fraudulent job postings.
The result is a small prototype system that analyzes job descriptions and estimates the likelihood that a posting may be fraudulent.

##  Motivation

Students searching for internships often encounter job postings that appear suspicious. These postings may include:

- unrealistic salary promises  
- vague job descriptions  
- requests for upfront payments  
- communication through personal messaging platforms  
- lack of company verification  

This project attempts to analyze job descriptions using **machine learning techniques** to highlight such warning signs.

---
## Tech Stack

This project was implemented using:

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Random Forest Classifier
- Streamlit

##  How the System Works

The system analyzes job descriptions in several stages.

### 1. Text Processing
Job descriptions are converted into numerical features using **TF-IDF vectorization**, which captures important words and phrases from the text.

### 2. Machine Learning Model
A **Random Forest classifier** is trained on job posting data to learn patterns that distinguish legitimate listings from fraudulent ones.

### 3. Risk Score Generation
Instead of returning only a binary prediction, the model generates a **fraud risk score** that estimates how suspicious the job posting may be.

### 4. Suspicious Phrase Detection
The system also scans for phrases commonly associated with scams such as:

- earn money fast
- work from home
- no experience needed
- contact via WhatsApp

This provides a layer of **explainability** so users can understand why a job posting may be flagged.
