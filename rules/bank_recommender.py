from rules.bank_profiles import BANK_PROFILES


def recommend_banks(
    cibil,
    foir,
    ltv,
    approval_probability
):

    recommendations = []

    for bank, profile in BANK_PROFILES.items():

        score = 0.0
        reasons = []

        # ------------------------------------------
        # CIBIL
        # ------------------------------------------

        if cibil >= profile["min_cibil"]:

            score += 30

            reasons.append(
                "CIBIL meets preferred threshold"
            )

        else:

            score += max(
                0,
                30 - (
                    profile["min_cibil"] - cibil
                ) * 0.20
            )

            reasons.append(
                "CIBIL is below preferred threshold"
            )

        # ------------------------------------------
        # FOIR
        # ------------------------------------------

        if foir <= profile["max_foir"]:

            score += 25

            reasons.append(
                "FOIR is within preferred range"
            )

        else:

            excess = (
                foir - profile["max_foir"]
            )

            score += max(
                0,
                25 - excess * 100
            )

            reasons.append(
                "FOIR is above preferred level"
            )

        # ------------------------------------------
        # LTV
        # ------------------------------------------

        if ltv <= profile["max_ltv"]:

            score += 25

            reasons.append(
                "LTV is within preferred range"
            )

        else:

            excess = (
                ltv - profile["max_ltv"]
            )

            score += max(
                0,
                25 - excess * 100
            )

            reasons.append(
                "LTV is above preferred level"
            )

        # ------------------------------------------
        # ML APPROVAL PROBABILITY
        # ------------------------------------------

        score += (
            approval_probability * 20
        )

        # ------------------------------------------
        # ELIGIBILITY
        # ------------------------------------------

        eligible = (

            cibil >= profile["min_cibil"]

            and

            foir <= profile["max_foir"]

            and

            ltv <= profile["max_ltv"]

        )

        # ------------------------------------------
        # Penalty for not meeting profile
        # ------------------------------------------

        if not eligible:

            score *= 0.65

            reasons.append(
                "Applicant does not meet all "
                "configured bank criteria"
            )

        score = max(
            0,
            min(score, 100)
        )

        recommendations.append({

            "bank": bank,

            "match_score": round(
                score,
                2
            ),

            "eligible": eligible,

            "reasons": reasons

        })

    # Highest score first

    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations