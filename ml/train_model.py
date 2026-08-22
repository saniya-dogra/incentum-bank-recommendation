# # ml/train_model.py
# import pandas as pd
# import joblib
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline

# df = pd.read_csv("ml/train.csv")

# X = df[["income", "cibil", "loan"]]
# y = df["approved"]

# model = Pipeline([
#     ("scaler", StandardScaler()),
#     ("clf", LogisticRegression(
#         max_iter=2000,
#         class_weight="balanced"
#     ))
# ])

# model.fit(X, y)
# joblib.dump(model, "ml/model.pkl")

# print("✅ Logistic Regression model trained")




import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)


# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("ml/train.csv")

print("Dataset shape:", df.shape)


# =========================================
# FEATURES
# =========================================

FEATURES = [
    "age",
    "income",
    "cibil",
    "loan",
    "existing_emi",
    "tenure",
    "property_age",
    "property_value",
    "foir",
    "ltv",
    "loan_to_income",
    "employment_type",
    "city_type"
]

TARGET = "approved"

X = df[FEATURES]
y = df[TARGET]


# =========================================
# FEATURE TYPES
# =========================================

numeric_features = [
    "age",
    "income",
    "cibil",
    "loan",
    "existing_emi",
    "tenure",
    "property_age",
    "property_value",
    "foir",
    "ltv",
    "loan_to_income"
]

categorical_features = [
    "employment_type",
    "city_type"
]


# =========================================
# PREPROCESSING
# =========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            StandardScaler(),
            numeric_features
        ),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# =========================================
# SINGLE ML MODEL
# =========================================

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced"
            )
        )
    ]
)


# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# =========================================
# TRAIN MODEL
# =========================================

print("\nTraining Logistic Regression Model...\n")

model.fit(X_train, y_train)


# =========================================
# EVALUATION
# =========================================

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)
roc = roc_auc_score(y_test, prob)

print("=" * 40)
print("MODEL EVALUATION")
print("=" * 40)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc:.4f}")

print("\nClassification Report\n")

print(classification_report(y_test, pred))


# =========================================
# SAVE MODEL
# =========================================

joblib.dump(model, "ml/model.pkl")

print("Model saved successfully to ml/model.pkl")