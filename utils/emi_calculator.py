def calculate_emi(P, annual_rate, years):
    r = annual_rate / (12 * 100)
    n = years * 12
    return (P * r * (1+r)**n) / ((1+r)**n - 1)
