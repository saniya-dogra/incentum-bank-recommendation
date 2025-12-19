from rules.age_rules import check_age
from rules.income_rules import check_income
from rules.employment_rules import check_employment
from rules.property_rules import check_property
from rules.ltv_rules import check_ltv
from rules.foir_rules import allowed_foir
from rules.roi_rules import get_roi
from utils.emi_calculator import calculate_emi

def bom_engine(data):
    for rule in [
        check_age(data["age"], data["employment_type"]),
        check_income(data["annual_income"]),
        check_employment(data["employment_type"], data.get("business_years",0), data.get("itr_years",0)),
        check_property(data["property_age"], data["city_type"], data["loan_category"])
    ]:
        if rule[0] is False:
            return False, rule[1]

    roi = get_roi(data["cibil"], data["employment_type"]=="salaried")
    emi = calculate_emi(data["loan_amount"], roi, data["tenure_years"])

    foir = (emi + data["existing_emi"]) / data["monthly_income"]
    if foir > allowed_foir(data["monthly_income"]):
        return False, "FOIR exceeds limit"

    ok, ltv = check_ltv(data["loan_amount"], data["property_cost"])
    if not ok:
        return False, "LTV exceeds limit"

    return True, {
        "roi": roi,
        "emi": round(emi,2),
        "foir": round(foir*100,2),
        "ltv": round(ltv*100,2)
    }
