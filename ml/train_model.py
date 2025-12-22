# ml/train_model.py
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv("ml/train.csv")

X = df[["income", "cibil", "loan"]]
y = df["approved"]

model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

model.fit(X, y)
joblib.dump(model, "ml/model.pkl")

print("✅ Logistic Regression model trained")
