from rules.bank_profiles import BANK_PROFILES

DEBUG = False

PORT = 5000

MODEL_PATH = "ml/model.pkl"

BANKS = list(BANK_PROFILES.keys())

MAX_LOAN_TENURE_YEARS = 30

MAX_AGE_AT_MATURITY = 75

CURRENCY = "INR"