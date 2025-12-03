import math

# Hardcoded exchange rates for demonstration purposes
HARDCODED_RATES = {
    "USD": {"PKR": 280.0, "EUR": 0.92, "GBP": 0.79, "USD": 1.0},
    "PKR": {"USD": 1/280.0, "EUR": 0.92/280.0, "GBP": 0.79/280.0, "PKR": 1.0},
    "EUR": {"USD": 1/0.92, "PKR": 280.0/0.92, "GBP": 0.79/0.92, "EUR": 1.0},
    "GBP": {"USD": 1/0.79, "PKR": 280.0/0.79, "EUR": 0.92/0.79, "GBP": 1.0},
}

def get_exchange_rates(base_currency="USD"):
    if base_currency in HARDCODED_RATES:
        return HARDCODED_RATES[base_currency]
    return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)

    if not rates:
        raise ValueError(f"Unsupported source currency: {from_currency}")

    if to_currency not in rates:
        raise ValueError(f"Unsupported target currency: {to_currency}")

    return amount * rates[to_currency]
