import random
import pandas as pd

ROWS = 20000


def cibil_strength(cibil):
    if cibil >= 800:
        return 1.00
    elif cibil >= 750:
        return 0.90
    elif cibil >= 725:
        return 0.80
    elif cibil >= 700:
        return 0.70
    elif cibil >= 650:
        return 0.50
    else:
        return 0.30


def calculate_emi(loan, annual_rate, tenure):
    monthly_rate = annual_rate / (12 * 100)
    months = tenure * 12

    if monthly_rate == 0:
        return loan / months

    return (
        loan
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )


def generate_row():

    age = random.randint(21, 65)

    income = random.randint(20000, 250000)

    cibil = random.randint(600, 850)

    loan = random.randint(300000, 8000000)

    existing_emi = random.randint(0, 40000)

    tenure = random.randint(5, 30)

    property_age = random.randint(0, 30)

    property_value = random.randint(
        max(loan, 1000000),
        max(loan + 500000, 10000000)
    )

    employment_type = random.choice([
        "salaried",
        "self_employed"
    ])

    city_type = random.choice([
        "metro",
        "non_metro"
    ])

    emi = calculate_emi(
        loan,
        8.5,
        tenure
    )

    foir = (
        emi + existing_emi
    ) / income

    ltv = loan / property_value

    loan_to_income = loan / (income * 12)

    score = 0

    # CIBIL
    score += (
        0.30
        * cibil_strength(cibil)
    )

    # Income
    income_strength = min(
        income / 250000,
        1
    )

    score += (
        0.20
        * income_strength
    )

    # FOIR
    if foir <= 0.40:
        foir_score = 1.0
    elif foir <= 0.50:
        foir_score = 0.75
    elif foir <= 0.60:
        foir_score = 0.50
    elif foir <= 0.70:
        foir_score = 0.25
    else:
        foir_score = 0.0

    score += (
        0.20
        * foir_score
    )

    # LTV
    if ltv <= 0.70:
        ltv_score = 1.0
    elif ltv <= 0.80:
        ltv_score = 0.75
    elif ltv <= 0.90:
        ltv_score = 0.50
    else:
        ltv_score = 0.0

    score += (
        0.15
        * ltv_score
    )

    # Loan-to-income
    if loan_to_income <= 3:
        lti_score = 1.0
    elif loan_to_income <= 5:
        lti_score = 0.70
    elif loan_to_income <= 7:
        lti_score = 0.40
    else:
        lti_score = 0.10

    score += (
        0.10
        * lti_score
    )

    # Employment stability
    if employment_type == "salaried":
        score += 0.05
    else:
        score += 0.02

    # Small noise
    noise = random.uniform(
        -0.08,
        0.08
    )

    final_score = max(
        0,
        min(
            score + noise,
            1
        )
    )

    approved = (
        1
        if random.random() < final_score
        else 0
    )

    return {
        "age": age,
        "income": income,
        "cibil": cibil,
        "loan": loan,
        "existing_emi": existing_emi,
        "tenure": tenure,
        "property_age": property_age,
        "property_value": property_value,
        "foir": round(foir, 4),
        "ltv": round(ltv, 4),
        "loan_to_income": round(
            loan_to_income,
            4
        ),
        "employment_type": employment_type,
        "city_type": city_type,
        "approved": approved
    }


def generate_dataset():

    rows = [
        generate_row()
        for _ in range(ROWS)
    ]

    df = pd.DataFrame(rows)

    print(
        "Dataset shape:",
        df.shape
    )

    print(
        "Approval ratio:",
        round(
            df["approved"].mean() * 100,
            2
        ),
        "%"
    )

    df.to_csv(
        "ml/train.csv",
        index=False
    )

    print(
        "Dataset saved to ml/train.csv"
    )


if __name__ == "__main__":
    generate_dataset()