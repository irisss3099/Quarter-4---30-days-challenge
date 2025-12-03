def convert_time(value, from_unit, to_unit):
    # Define conversion factors to a base unit (e.g., seconds)
    conversion_factors = {
        "s": 1,             # 1 second = 1 second
        "min": 60,          # 1 minute = 60 seconds
        "hr": 3600,         # 1 hour = 3600 seconds
        "day": 86400,       # 1 day = 86400 seconds
        "week": 604800,     # 1 week = 604800 seconds
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided. Supported units are s, min, hr, day, week.")

    # Convert the value to the base unit (seconds)
    value_in_seconds = value * conversion_factors[from_unit]

    # Convert from the base unit (seconds) to the target unit
    converted_value = value_in_seconds / conversion_factors[to_unit]

    return converted_value
