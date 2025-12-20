# rules/eligibility_engine.py

from rules.age_rules import check_age
from rules.income_rules import check_income
from rules.employment_rules import check_employment
from rules.property_rules import check_property
from rules.ltv_rules import check_ltv
from rules.foir_rules import allowed_foir
from rules.roi_rules import get_roi
from rules.special_cases import (
    pensioner_rules,
    agriculturist_rules,
    cre_penalty,
    green_building_concession
)
from utils.emi_calculator import calculate_emi


def bom_engine(data):
    """
    Bank of Maharashtra Home Loan Eligibility Engine
    Applies ALL automatable rules from the official PDF
    """

    # -------------------------------------------------
    # 1️⃣ BASIC ELIGIBILITY CHECKS
    # -------------------------------------------------
    checks = [
        check_age(data["age"], data["employment_type"]),
        check_income(data["annual_income"]),
        check_employment(
            data["employment_type"],
            data.get("business_years", 0),
            data.get("itr_years", 0)
        ),
        check_property(
            data["property_age"],
            data["city_type"],
            data["loan_category"]
        )
    ]

    for ok, msg in checks:
        if not ok:
            return False, msg

    # -------------------------------------------------
    # 2️⃣ SPECIAL EMPLOYMENT CASES (PDF)
    # -------------------------------------------------

    # Pensioner rules
    if data["employment_type"] == "pensioner":
        ok, msg = pensioner_rules(
            data.get("monthly_income", 0),
            data["age"]
        )
        if not ok:
            return False, msg

    # Agriculturist rules
    if data["employment_type"] == "agriculturist":
        ok, msg = agriculturist_rules(
            data["annual_income"],
            data.get("has_income_certificate", False)
        )
        if not ok:
            return False, msg

    # -------------------------------------------------
    # 3️⃣ ROI CALCULATION (BASE + PDF ADJUSTMENTS)
    # -------------------------------------------------
    roi = get_roi(
        data["cibil"],
        data["employment_type"] == "salaried"
    )

    # PDF adjustments
    roi += cre_penalty(data.get("is_third_property", False))
    roi += green_building_concession(data.get("green_building", False))

    # -------------------------------------------------
    # 4️⃣ EMI CALCULATION
    # -------------------------------------------------
    emi = calculate_emi(
        data["loan_amount"],
        roi,
        data["tenure_years"]
    )

    # -------------------------------------------------
    # 5️⃣ FOIR CHECK
    # -------------------------------------------------
    foir = (emi + data["existing_emi"]) / data["monthly_income"]

    if foir > allowed_foir(data["monthly_income"]):
        return False, "FOIR exceeds permissible limit"

    # -------------------------------------------------
    # 6️⃣ LTV CHECK
    # -------------------------------------------------
    ok, ltv = check_ltv(
        data["loan_amount"],
        data["property_cost"]
    )

    if not ok:
        return False, "LTV exceeds permissible limit"

    # -------------------------------------------------
    # ✅ ELIGIBLE → RETURN DETAILS
    # -------------------------------------------------
    return True, {
        "roi": round(roi, 2),
        "emi": round(emi, 2),
        "foir": round(foir * 100, 2),
        "ltv": round(ltv * 100, 2)
    }
