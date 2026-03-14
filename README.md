# Fake internship-job-scam-detector
As a student actively applying for internships and jobs, I often came across opportunities that seemed suspicious — especially “work from home” roles promising unrealistic salaries or asking candidates to contact recruiters through personal messaging platforms.

This project was built to explore whether machine learning and natural language processing (NLP) could help identify patterns commonly found in fraudulent job postings.

The result is a small prototype system that analyzes job descriptions and estimates the likelihood that a posting may be fraudulent.

The application provides:

a fraud risk score

detection of suspicious phrases

a simple interactive web interface

The goal is not to replace human judgment but to assist students in evaluating potentially risky job opportunities.

Motivation

Many students apply to internships through online platforms where job authenticity is not always guaranteed. Fake job postings can involve:

unrealistic salary promises

requests for upfront payments

vague company information

communication through personal messaging apps

This project explores how text-based analysis of job descriptions can help detect such warning signals.

How the System Works

The system processes job descriptions using Natural Language Processing (NLP) techniques.

1. Data Processing

Job descriptions are cleaned and transformed into numerical features using TF-IDF vectorization.

2. Machine Learning Model

A Random Forest classifier is trained to learn patterns associated with legitimate and fraudulent job postings.

3. Risk Scoring

Instead of only producing a binary prediction, the system generates a fraud risk score that indicates the probability of a job posting being suspicious.

4. Keyword Analysis

In addition to the ML model, the system checks for common scam phrases such as:

“earn money fast”

“work from home”

“no experience required”

“contact on WhatsApp”

This adds a layer of explainability, helping users understand why a job may be flagged.
