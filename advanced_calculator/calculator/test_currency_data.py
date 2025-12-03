def get_fake_exchange_rates(base_currency="USD"):
    if base_currency == "USD":
        return {
            "USD": 1.0,
            "PKR": 280.0,
            "EUR": 0.92,
            "GBP": 0.79
        }
    elif base_currency == "PKR":
        return {
            "USD": 1/280.0,
            "PKR": 1.0,
            "EUR": 0.92/280.0,
            "GBP": 0.79/280.0
        }
    elif base_currency == "EUR":
        return {
            "USD": 1/0.92,
            "PKR": 280.0/0.92,
            "EUR": 1.0,
            "GBP": 0.79/0.92
        }
    else:
        return {"USD": 1.0}

def generate_currency_conversion_test_cases():
    return [
        {"amount": 100, "from_currency": "USD", "to_currency": "PKR", "expected_rate": 280.0},
        {"amount": 50, "from_currency": "PKR", "to_currency": "USD", "expected_rate": 1/280.0},
        {"amount": 200, "from_currency": "EUR", "to_currency": "USD", "expected_rate": 1/0.92},
        {"amount": 75, "from_currency": "USD", "to_currency": "EUR", "expected_rate": 0.92},
        {"amount": 10, "from_currency": "GBP", "to_currency": "USD", "expected_rate": 1/0.79},
    ]
