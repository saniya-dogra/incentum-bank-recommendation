# ml/model.py

import joblib
from config import MODEL_PATH


class ApprovalModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict_probability(self, monthly_income, cibil, loan_amount):
        X = [[monthly_income, cibil, loan_amount]]
        probability = self.model.predict_proba(X)[0][1]
        return round(probability, 4)
