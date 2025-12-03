def convert_weight(value, from_unit, to_unit):
    # Define conversion factors to a base unit (e.g., grams)
    conversion_factors = {
        "kg": 1000,     # 1 kg = 1000 grams
        "g": 1,         # 1 g = 1 gram
        "mg": 0.001,    # 1 mg = 0.001 grams
        "lb": 453.592,  # 1 lb = 453.592 grams
        "oz": 28.3495,  # 1 oz = 28.3495 grams
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided. Supported units are kg, g, mg, lb, oz.")

    # Convert the value to the base unit (grams)
    value_in_grams = value * conversion_factors[from_unit]

    # Convert from the base unit (grams) to the target unit
    converted_value = value_in_grams / conversion_factors[to_unit]

    return converted_value
