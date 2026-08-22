"""
ml/generate_training_data.py

NOTE: Approval labels here are synthetically generated using a
hand-designed risk-scoring formula (weighted combination of income,
CIBIL risk tier, and loan-size penalty) — not derived from real
historical bank approval data or from the rule engine itself.

This was a deliberate choice for this demo project since real approval
data isn't available. A natural next step would be to either train on
real anonymized data, or generate labels directly via bom_engine()
eligibility outcomes for tighter alignment with the rule engine.
"""





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
