def get_roi(cibil, salaried=True):
    if cibil >= 800: return 8.35 if salaried else 8.45
    if cibil >= 750: return 8.40 if salaried else 8.50
    if cibil >= 725: return 8.80 if salaried else 8.90
    if cibil >= 700: return 9.30 if salaried else 9.50
    if cibil >= 650: return 9.80 if salaried else 10.00
    return 10.40 if salaried else 10.90
