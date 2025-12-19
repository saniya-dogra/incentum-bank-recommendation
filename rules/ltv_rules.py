def max_ltv(loan_amount):
    if loan_amount <= 3000000:
        return 0.90
    elif loan_amount <= 7500000:
        return 0.80
    else:
        return 0.75

def check_ltv(loan_amount, property_cost):
    ltv = loan_amount / property_cost
    return ltv <= max_ltv(loan_amount), ltv
