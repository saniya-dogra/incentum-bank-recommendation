# ml/model.py

import joblib

MODEL_PATH = "ml/model.pkl"


class ApprovalModel:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model = joblib.load(model_path)

    def predict_probability(self, monthly_income, cibil, loan_amount):
        X = [[monthly_income, cibil, loan_amount]]
        probability = self.model.predict_proba(X)[0][1]
        return round(probability, 4)