def convert_length(value, from_unit, to_unit):
    # Define conversion factors to a base unit (e.g., meters)
    conversion_factors = {
        "m": 1,         # 1 meter = 1 meter
        "cm": 0.01,     # 1 cm = 0.01 meters
        "km": 1000,     # 1 km = 1000 meters
        "inch": 0.0254, # 1 inch = 0.0254 meters
        "ft": 0.3048,   # 1 foot = 0.3048 meters
        "yd": 0.9144,   # 1 yard = 0.9144 meters
        "mile": 1609.34 # 1 mile = 1609.34 meters
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided. Supported units are m, cm, km, inch, ft, yd, mile.")

    # Convert the value to the base unit (meters)
    value_in_meters = value * conversion_factors[from_unit]

    # Convert from the base unit (meters) to the target unit
    converted_value = value_in_meters / conversion_factors[to_unit]

    return converted_value
