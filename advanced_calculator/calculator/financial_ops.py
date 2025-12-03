def simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")
    # Simple Interest = P * R * T
    return principal * rate * time

def compound_interest(principal, rate, time, n):
    if principal < 0 or rate < 0 or time < 0 or n <= 0:
        raise ValueError("Principal, rate, and time must be non-negative; n must be positive.")
    # Compound Interest = P * (1 + R/n)^(n*T) - P
    # A = P * (1 + R/n)^(n*T)
    amount = principal * (1 + rate / n)**(n * time)
    return amount - principal

def loan_payment(principal, annual_rate, loan_term_years):
    if principal < 0 or annual_rate < 0 or loan_term_years <= 0:
        raise ValueError("Principal, annual rate must be non-negative; loan term must be positive.")
    # Monthly payment for a fixed-rate loan
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    monthly_rate = annual_rate / 12
    number_of_payments = loan_term_years * 12

    if monthly_rate == 0:
        return principal / number_of_payments

    payment = principal * (monthly_rate * (1 + monthly_rate)**number_of_payments) / (((1 + monthly_rate)**number_of_payments) - 1)
    return payment
