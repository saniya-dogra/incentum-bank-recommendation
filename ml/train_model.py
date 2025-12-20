from sklearn.ensemble import RandomForestClassifier
import pandas as pd, joblib

df = pd.read_csv("ml/train.csv")
X = df[["income","cibil","loan"]]
y = df["approved"]

model = RandomForestClassifier(n_estimators=300)
model.fit(X,y)
joblib.dump(model, "ml/model.pkl")
