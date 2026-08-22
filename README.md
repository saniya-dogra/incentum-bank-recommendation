# AI Fintech Risk Manager

### Explainable ML-Based Loan Risk Assessment and Multi-Bank Recommendation System

An AI-powered fintech risk assessment system that evaluates a loan applicant's financial profile, predicts approval probability using Machine Learning, calculates financial risk, explains the major risk factors, and recommends the most suitable bank based on configurable lending profiles.

---

## 🎯 Project Overview

Financial institutions need to evaluate applicants using multiple financial indicators such as credit score, income, existing liabilities, loan amount, property value, and repayment capacity.

This project combines:

- Machine Learning
- Financial risk rules
- Explainable risk assessment
- Multi-bank recommendation
- REST API

to create an end-to-end **AI Fintech Risk Manager**.

The system does not simply predict loan approval. It combines the ML prediction with financial risk indicators and bank-specific configurable profiles to produce an explainable recommendation.

---

## 🚀 Key Features

### 1. AI-Based Approval Prediction

A Logistic Regression model predicts the probability of loan approval using financial and applicant-level features.

The model uses:

- Age
- Income
- CIBIL score
- Loan amount
- Existing EMI
- Loan tenure
- Property age
- Property value
- FOIR
- LTV
- Loan-to-income ratio
- Employment type
- City type

---

### 2. Financial Risk Assessment

The system calculates a risk score using:

- ML approval probability
- CIBIL score
- FOIR
- Loan-to-Value ratio
- Loan-to-Income ratio

The applicant is categorized as:

- LOW RISK
- MEDIUM RISK
- HIGH RISK

---

### 3. Explainable Risk Assessment

Instead of only returning a prediction, the system explains the major factors influencing the assessment.

Example:

```text
Strong CIBIL score
FOIR is within a comfortable range
Moderately high loan-to-value ratio
Loan-to-income ratio is reasonable