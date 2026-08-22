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

The system goes beyond a simple loan approval prediction by combining the ML prediction with financial risk indicators and bank-specific configurable profiles to produce an explainable recommendation.

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
```

---

## 🏦 4. Multi-Bank Recommendation

The system evaluates the applicant against configurable profiles of multiple banks and calculates a match score based on the applicant's financial profile.

Currently supported banks:

- Bank of Maharashtra
- State Bank of India
- HDFC Bank
- ICICI Bank

The highest-scoring eligible bank is selected as the final recommendation.

Example:

```text
Bank of Maharashtra
Match Score : 97.92
Status      : ELIGIBLE

State Bank of India
Match Score : 60.86
Status      : NOT ELIGIBLE

HDFC Bank
Match Score : 57.61
Status      : NOT ELIGIBLE

ICICI Bank
Match Score : 57.61
Status      : NOT ELIGIBLE
```

> Bank profiles are configurable prototype policies and do not represent official lending criteria.

---

## 🤖 5. Machine Learning Model

The project uses a **Logistic Regression** model for loan approval prediction.

### Model Evaluation

- Accuracy: **67.33%**
- Precision: **79.56%**
- Recall: **67.29%**
- F1 Score: **72.91%**
- ROC-AUC: **73.14%**

The training dataset is synthetically generated for the project.

> The approval probability shown for an individual applicant is different from the overall model accuracy.

---

## 🎯 6. Working Example

### Applicant Financial Profile

```text
Age               : 30
Employment        : salaried
Monthly Income    : ₹300,000
CIBIL Score       : 780
Loan Amount       : ₹2,500,000
Existing EMI      : ₹5,000
Tenure            : 20 years
```

### Financial Analysis

```text
Interest Rate     : 8.4%
Monthly EMI       : ₹21,537.61
FOIR              : 8.85%
LTV               : 89.29%
Loan/Income Ratio : 0.69
```

### AI Risk Assessment

```text
Approval Probability : 89.61%
Risk Score           : 17.64
Risk Level           : LOW
Recommended Action   : RECOMMEND_APPROVAL
```

### Risk Factors

```text
• Strong CIBIL score
• FOIR is within a comfortable range
• Moderately high loan-to-value ratio
• Loan-to-income ratio is reasonable
```

### Final Recommendation

```text
🏆 Bank of Maharashtra
Match Score : 97.92
Status      : ELIGIBLE
```

---

## 🛠️ 7. Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Flask
- Joblib
- REST API
- Git & GitHub