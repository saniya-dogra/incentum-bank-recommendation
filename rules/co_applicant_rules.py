def process_co_applicants(data):
    """
    Combines income of all applicants
    Determines youngest earning applicant (for tenure)
    """

    total_income = data["monthly_income"]
    youngest_age = data["age"]

    co_apps = data.get("co_applicants", [])

    # Bank allows max 5 applicants (1 primary + 4 co-applicants)
    if len(co_apps) > 4:
        return False, "Maximum 5 applicants allowed", None, None

    for person in co_apps:
        if person["monthly_income"] <= 0:
            return False, "Invalid co-applicant income", None, None

        total_income += person["monthly_income"]
        youngest_age = min(youngest_age, person["age"])

    return True, None, total_income, youngest_age
