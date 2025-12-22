# ml/generate_training_data.py

# import random
# import pandas as pd

# from rules.eligibility_engine import bom_engine

# ROWS = 5000   # You can increase to 10k later

# def generate_row():
#     age = random.randint(21, 65)
#     employment_type = random.choice(["salaried", "self_employed"])

#     monthly_income = random.randint(20000, 200000)
#     annual_income = monthly_income * 12

#     cibil = random.randint(600, 850)

#     loan_amount = random.randint(500000, 8000000)
#     property_cost = loan_amount + random.randint(100000, 2000000)

#     property_age = random.randint(0, 30)
#     city_type = random.choice(["metro", "non_metro"])

#     tenure_years = random.randint(5, 30)
#     existing_emi = random.randint(0, 15000)

#     data = {
#         "age": age,
#         "employment_type": employment_type,
#         "monthly_income": monthly_income,
#         "annual_income": annual_income,
#         "cibil": cibil,
#         "loan_amount": loan_amount,
#         "property_cost": property_cost,
#         "property_age": property_age,
#         "city_type": city_type,
#         "existing_emi": existing_emi,
#         "tenure_years": tenure_years,
#         "loan_category": "purchase",
#         "green_building": random.choice([True, False]),
#         "is_third_property": random.choice([True, False]),
#         "topup_loan": False
#     }

#     eligible, _ = bom_engine(data)

#     return {
#         "income": monthly_income,
#         "cibil": cibil,
#         "loan": loan_amount,
#         "approved": 1 if eligible else 0
#     }


# def generate_dataset():
#     rows = []

#     for _ in range(ROWS):
#         rows.append(generate_row())

#     df = pd.DataFrame(rows)
#     df.to_csv("ml/train.csv", index=False)
#     print(f"✅ Training data generated: {ROWS} rows saved to ml/train.csv")


# if __name__ == "__main__":
#     generate_dataset()
# # ml/generate_training_data.py

# import random
# import pandas as pd

# from rules.eligibility_engine import bom_engine

# ROWS = 5000   # You can increase to 10k later

# def generate_row():
#     age = random.randint(21, 65)
#     employment_type = random.choice(["salaried", "self_employed"])

#     monthly_income = random.randint(20000, 200000)
#     annual_income = monthly_income * 12

#     cibil = random.randint(600, 850)

#     loan_amount = random.randint(500000, 8000000)
#     property_cost = loan_amount + random.randint(100000, 2000000)

#     property_age = random.randint(0, 30)
#     city_type = random.choice(["metro", "non_metro"])

#     tenure_years = random.randint(5, 30)
#     existing_emi = random.randint(0, 15000)

#     data = {
#         "age": age,
#         "employment_type": employment_type,
#         "monthly_income": monthly_income,
#         "annual_income": annual_income,
#         "cibil": cibil,
#         "loan_amount": loan_amount,
#         "property_cost": property_cost,
#         "property_age": property_age,
#         "city_type": city_type,
#         "existing_emi": existing_emi,
#         "tenure_years": tenure_years,
#         "loan_category": "purchase",
#         "green_building": random.choice([True, False]),
#         "is_third_property": random.choice([True, False]),
#         "topup_loan": False
#     }

#     eligible, _ = bom_engine(data)

#     return {
#         "income": monthly_income,
#         "cibil": cibil,
#         "loan": loan_amount,
#         "approved": 1 if eligible else 0
#     }


# def generate_dataset():
#     rows = []

#     for _ in range(ROWS):
#         rows.append(generate_row())

#     df = pd.DataFrame(rows)
#     df.to_csv("ml/train.csv", index=False)
#     print(f"✅ Training data generated: {ROWS} rows saved to ml/train.csv")


# if __name__ == "__main__":
#     generate_dataset()



import random
import pandas as pd

ROWS = 20000   # higher = more stable model


# -------------------------------------------------
# PDF-aligned CIBIL → risk strength
# (lower ROI = lower risk)
# -------------------------------------------------
def cibil_risk_weight(cibil):
    if cibil >= 800:
        return 1.00
    elif cibil >= 750:
        return 0.95
    elif cibil >= 725:
        return 0.85
    elif cibil >= 700:
        return 0.70
    elif cibil >= 650:
        return 0.55
    else:
        return 0.35


def generate_row():
    income = random.randint(20000, 200000)
    cibil = random.randint(600, 850)
    loan = random.randint(500000, 8000000)

    # Normalize features
    income_score = income / 200000
    loan_penalty = loan / 8000000
    cibil_score = cibil_risk_weight(cibil)

    # PDF-consistent risk score
    score = (
        0.4 * income_score +
        0.4 * cibil_score -
        0.3 * loan_penalty
    )

    # Clamp score
    score = max(min(score, 1), 0)

    # ✅ Probabilistic approval → balanced data
    approved = 1 if random.random() < score else 0

    return {
        "income": income,
        "cibil": cibil,
        "loan": loan,
        "approved": approved
    }


def generate_dataset():
    rows = [generate_row() for _ in range(ROWS)]
    df = pd.DataFrame(rows)

    print("Approved ratio:", round(df["approved"].mean(), 2))

    df.to_csv("ml/train.csv", index=False)
    print("✅ Training data generated with FIXED CIBIL logic")


if __name__ == "__main__":
    generate_dataset()
