# AI Fintech Risk Manager

### Explainable ML-Based Loan Risk Assessment & Multi-Bank Recommendation

An AI-powered fintech system that evaluates a loan applicant's financial profile, predicts loan approval probability using Machine Learning, calculates financial risk, explains the key risk factors, and recommends compatible lenders.

---

## 🎯 Problem

Loan assessment depends on multiple factors such as credit score, income, existing liabilities, loan amount, property value, and repayment capacity.

A simple approval prediction does not explain **why an applicant is risky** or **which lender may be more suitable**.

This project combines **Machine Learning + financial rules + explainable risk scoring** to provide a more transparent loan risk assessment.

---

## 💡 How It Works

```text
Applicant Details
       ↓
Input Validation
       ↓
Eligibility Rules
       ↓
EMI / FOIR / LTV Calculation
       ↓
Logistic Regression
       ↓
Approval Probability
       ↓
Risk Score & Explanation
       ↓
Bank Compatibility Matching
```

The system uses two complementary approaches:

* **Rule-based checks** handle hard eligibility constraints.
* **Machine Learning** estimates approval probability for eligible applicants.
* **Risk scoring** combines ML output with important financial indicators.
* **Bank matching** compares the applicant against configurable lender profiles.

---

## 🚀 Key Features

### 1. AI-Based Approval Prediction

A **Logistic Regression** model predicts loan approval probability using:

* Age
* Income
* CIBIL score
* Loan amount
* Existing EMI
* Loan tenure
* Property age
* Property value
* FOIR
* LTV
* Loan-to-income ratio
* Employment type
* City type

### 2. Financial Risk Assessment

The system calculates:

**FOIR**

```text
(New EMI + Existing EMI) / Monthly Income
```

**LTV**

```text
Loan Amount / Effective Property Value
```

**Loan-to-Income**

```text
Loan Amount / Annual Income
```

These indicators are combined with the ML prediction to generate a risk score.

### 3. Explainable Risk Assessment

The system provides understandable reasons behind the assessment, for example:

```text
Strong CIBIL score
FOIR is within a comfortable range
Moderately high loan-to-value ratio
Loan-to-income ratio is reasonable
```

### 4. Multi-Bank Recommendation

The applicant is compared against configurable profiles for:

* Bank of Maharashtra
* State Bank of India
* HDFC Bank
* ICICI Bank

Each profile contains parameters such as minimum CIBIL, maximum FOIR, and maximum LTV.

> Bank profiles are prototype configurations created for demonstration and do not represent official lending criteria.

---

## 🤖 Machine Learning

### Model

**Logistic Regression**

It was selected because the task is binary classification and the model provides an interpretable probability output while remaining lightweight and easy to evaluate.

### Dataset

The project uses **20,000 synthetically generated applicant records**.

Synthetic data is used because real lending data contains sensitive financial information and is not available for this student project.

### Model Performance

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 66.80% |
| Precision | 80.31% |
| Recall    | 65.59% |
| F1 Score  | 72.21% |
| ROC-AUC   | 72.50% |

> These results are based on the synthetic dataset and should not be interpreted as production lending performance.

---

## 📊 Risk Decision

The final risk score combines:

```text
35% → ML Risk
20% → CIBIL Risk
20% → FOIR Risk
20% → LTV Risk
 5% → Loan-to-Income Risk
```

The result is classified as:

```text
LOW     → Recommend Approval
MEDIUM  → Manual Review
HIGH    → Reject or Verify
```

Hard eligibility failures are rejected before the ML risk assessment stage.

---

## 🧪 Demo

### Strong Applicant

```text
CIBIL              : 780
Monthly Income     : ₹300,000
Loan Amount        : ₹2,500,000
Existing EMI       : ₹5,000
Tenure             : 20 years
```

Result:

```text
Approval Probability : 91.37%
Risk Score           : 17.02
Risk Level           : LOW
Decision              : RECOMMEND_APPROVAL
```

**Recommended Bank:** Bank of Maharashtra

**Match Score:** 98.27

---

### Medium-Risk Applicant

```text
CIBIL              : 660
Monthly Income     : ₹70,000
Loan Amount        : ₹2,500,000
Existing EMI       : ₹15,000
Tenure             : 20 years
```

Result:

```text
Approval Probability : 34.73%
Risk Score           : 43.85
Risk Level           : MEDIUM
Decision              : MANUAL_REVIEW
```

---

### Hard Eligibility Failure

A salaried applicant aged 63 fails the configured retirement-age rule.

```text
Decision: REJECTED
Reason: Age exceeds retirement age
```

This applicant does not proceed to the ML risk assessment stage.

---

## 🔧 Development Challenge

During development, one issue was identified in the processing flow: applicants who failed hard eligibility rules could potentially continue toward later stages of the pipeline.

The Flask API was updated so that the eligibility engine acts as a clear gate:

```text
Eligibility Failed
       ↓
REJECTED
```

while eligible applicants continue to:

```text
Financial Metrics
       ↓
ML Prediction
       ↓
Risk Assessment
       ↓
Bank Recommendation
```

This made the decision flow more consistent and easier to explain.

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **Joblib**
* **Requests**
* **REST API**
* **Git & GitHub**

---

## 📁 Project Structure

```text
incentum-bank-recommendation/
│
├── backend/
│   ├── app.py
│   └── config.py
│
├── ml/
│   ├── generate_training_data.py
│   ├── train_model.py
│   ├── train.csv
│   └── model.pkl
│
├── rules/
│   ├── age_rules.py
│   ├── bank_profiles.py
│   ├── bank_recommender.py
│   ├── co_applicant_rules.py
│   ├── eligibility_engine.py
│   ├── employment_rules.py
│   ├── foir_rules.py
│   ├── income_rules.py
│   ├── loan_purpose_rules.py
│   ├── ltv_rules.py
│   ├── property_rules.py
│   ├── residual_life_rules.py
│   ├── risk_engine.py
│   ├── roi_rules.py
│   ├── special_cases.py
│   └── tenure_rules.py
│
├── utils/
│   ├── emi_calculator.py
│   └── validators.py
│
├── test_bank_recommendation.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate training data

```bash
python ml/generate_training_data.py
```

### 3. Train the model

```bash
python ml/train_model.py
```

### 4. Start the Flask API

```bash
python -m backend.app
```

### 5. Run the test cases

Open another terminal:

```bash
python test_bank_recommendation.py
```

The test script demonstrates approved, rejected, and medium-risk applicants.

---

## 🔌 API

### Health Check

```http
GET /health
```

### Loan Risk Assessment

```http
POST /recommend
```

The API returns:

* Decision
* Approval probability
* Risk score
* Risk level
* Risk factors
* Financial metrics
* Bank recommendations

---

## ⚠️ Limitations

This is a **student-level fintech prototype**.

* The ML model is trained on synthetic data.
* Bank profiles are configurable demonstration policies.
* The model is not intended for real lending decisions.
* Production use would require validated historical lending data, model monitoring, fairness testing, security controls, and regulatory compliance.

---

## 👩‍💻 Author

**Saniya Dogra**

AI • Machine Learning • Software Engineering • FinTech
