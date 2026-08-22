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

    if cibil < 700:

        factors.append(
            "Low CIBIL score increases credit risk"
        )

    elif cibil < 750:

        factors.append(
            "Moderate CIBIL score"
        )

    else:

        factors.append(
            "Strong CIBIL score"
        )


    # ==========================================
    # FOIR
    # ==========================================

    if foir > 0.70:

        factors.append(
            "High FOIR indicates high repayment burden"
        )

    elif foir > 0.60:

        factors.append(
            "FOIR is moderately high"
        )

    else:

        factors.append(
            "FOIR is within a comfortable range"
        )


    # ==========================================
    # LTV
    # ==========================================

    if ltv > 0.90:

        factors.append(
            "High loan-to-value ratio"
        )

    elif ltv > 0.80:

        factors.append(
            "Moderately high loan-to-value ratio"
        )

    else:

        factors.append(
            "Loan-to-value ratio is within "
            "a comfortable range"
        )


    # ==========================================
    # Loan-to-income
    # ==========================================

    if loan_to_income > 7:

        factors.append(
            "Loan amount is high compared "
            "to annual income"
        )

    elif loan_to_income > 5:

        factors.append(
            "Loan-to-income ratio requires attention"
        )

    else:

        factors.append(
            "Loan-to-income ratio is reasonable"
        )


    return factors