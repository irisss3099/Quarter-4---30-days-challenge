def is_valid_number(value):
    """Checks if a value can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_positive(value, name="Value"):
    """Validates that a numerical value is positive."""
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{name} must be a positive number.")

def validate_non_negative(value, name="Value"):
    """Validates that a numerical value is non-negative."""
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{name} must be a non-negative number.")

def validate_not_zero(value, name="Value"):
    """Validates that a numerical value is not zero."""
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
