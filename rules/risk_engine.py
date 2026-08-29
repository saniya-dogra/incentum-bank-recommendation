def calculate_risk(
    approval_probability,
    foir,
    ltv,
    cibil,
    loan_to_income
):
    

    # ==========================================
    # 1. ML MODEL RISK
    # ==========================================

    ml_risk = (
        1 - approval_probability
    ) * 100


    # ==========================================
    # 2. CIBIL RISK
    # ==========================================

    if cibil >= 800:

        cibil_risk = 0

    elif cibil >= 750:

        cibil_risk = 15

    elif cibil >= 700:

        cibil_risk = 30

    elif cibil >= 650:

        cibil_risk = 55

    else:

        cibil_risk = 80


    # ==========================================
    # 3. FOIR RISK
    # ==========================================

    if foir <= 0.50:

        foir_risk = 0

    elif foir <= 0.60:

        foir_risk = 25

    elif foir <= 0.70:

        foir_risk = 50

    else:

        foir_risk = 90


    # ==========================================
    # 4. LTV RISK
    # ==========================================

    if ltv <= 0.70:

        ltv_risk = 0

    elif ltv <= 0.80:

        ltv_risk = 25

    elif ltv <= 0.90:

        ltv_risk = 55

    else:

        ltv_risk = 90


    # ==========================================
    # 5. LOAN-TO-INCOME RISK
    # ==========================================

    if loan_to_income <= 3:

        lti_risk = 0

    elif loan_to_income <= 5:

        lti_risk = 25

    elif loan_to_income <= 7:

        lti_risk = 50

    else:

        lti_risk = 80


    # ==========================================
    # 6. WEIGHTED RISK SCORE
    # ==========================================

    risk_score = (

        0.35 * ml_risk

        + 0.20 * cibil_risk

        + 0.20 * foir_risk

        + 0.20 * ltv_risk

        + 0.05 * lti_risk

    )


    risk_score = max(
        0,
        min(
            risk_score,
            100
        )
    )


    risk_score = round(
        risk_score,
        2
    )


    # ==========================================
    # 7. RISK LEVEL
    # ==========================================

    if risk_score < 30:

        risk_level = "LOW"

        recommended_action = (
    "RECOMMEND_APPROVAL"
)

    elif risk_score < 60:

        risk_level = "MEDIUM"

        recommended_action = (
            "MANUAL_REVIEW"
        )


    else:

        risk_level = "HIGH"

        recommended_action = (
            "REJECT_OR_VERIFY"
        )


    return {

        "risk_score":
            risk_score,

        "risk_level":
            risk_level,

        "recommended_action":
            recommended_action

    }


def explain_risk(
    cibil,
    foir,
    ltv,
    loan_to_income
):

    factors = []

    # ==========================================
    # CIBIL
    # ==========================================

    if cibil < 650:

        factors.append(
            f"CIBIL {cibil}: High credit risk"
        )

    elif cibil < 700:

        factors.append(
            f"CIBIL {cibil}: Below preferred range"
        )

    elif cibil < 750:

        factors.append(
            f"CIBIL {cibil}: Moderate credit strength"
        )

    else:

        factors.append(
            f"CIBIL {cibil}: Strong credit profile"
        )


    # ==========================================
    # FOIR
    # ==========================================

    foir_percent = round(
        foir * 100,
        2
    )

    if foir > 0.70:

        factors.append(
            f"FOIR {foir_percent}%: High repayment burden"
        )

    elif foir > 0.60:

        factors.append(
            f"FOIR {foir_percent}%: Elevated repayment burden"
        )

    elif foir > 0.50:

        factors.append(
            f"FOIR {foir_percent}%: Moderately high repayment burden"
        )

    else:

        factors.append(
            f"FOIR {foir_percent}%: Comfortable repayment burden"
        )


    # ==========================================
    # LTV
    # ==========================================

    ltv_percent = round(
        ltv * 100,
        2
    )

    if ltv > 0.90:

        factors.append(
            f"LTV {ltv_percent}%: High loan-to-value risk"
        )

    elif ltv > 0.80:

        factors.append(
            f"LTV {ltv_percent}%: Moderately high"
        )

    else:

        factors.append(
            f"LTV {ltv_percent}%: Within comfortable range"
        )


    # ==========================================
    # LOAN TO INCOME
    # ==========================================

    lti_rounded = round(
        loan_to_income,
        2
    )

    if loan_to_income > 7:

        factors.append(
            f"Loan-to-income {lti_rounded}: High"
        )

    elif loan_to_income > 5:

        factors.append(
            f"Loan-to-income {lti_rounded}: Requires attention"
        )

    else:

        factors.append(
            f"Loan-to-income {lti_rounded}: Reasonable"
        )
    return factors