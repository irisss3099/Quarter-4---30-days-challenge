# Data Model: Advanced CLI & Streamlit Calculator

**Feature Branch**: `1-advanced-calculator-features`
**Date**: 2025-12-03

## Key Concepts and Data Structures

This feature primarily deals with mathematical operations and conversions on numerical data. Traditional persistent data entities are not central to this application. Instead, the focus is on input/output data structures and conversion factors.

### 1. Calculation Input

*   **Description**: Represents the input parameters for any calculation or conversion.
*   **Attributes**:
    *   `value`: (Float) The primary numerical value for an operation (e.g., amount, angle, number).
    *   `operand`: (Float, Optional) The second numerical value for binary operations (e.g., in arithmetic or power functions).
    *   `operation`: (String) The specific arithmetic, scientific, or financial operation to perform.
    *   `from_unit`: (String, Optional) The source unit for conversions (e.g., "USD", "kg", "m", "s").
    *   `to_unit`: (String, Optional) The target unit for conversions (e.g., "EUR", "lb", "ft", "hr").
    *   `base_currency`: (String, Optional) The base currency for fetching exchange rates.
    *   `compounding_frequency`: (Integer, Optional) Number of times interest is compounded per year for financial calculations.
    *   `loan_term_years`: (Float, Optional) Term of a loan in years for financial calculations.
*   **Validation Rules**:
    *   Numerical values must be valid numbers (`is_valid_number`).
    *   Inputs must adhere to specific domain constraints (e.g., positive for square root, non-negative for principal, non-zero for division).
    *   Units/currencies must be recognized and supported.

### 2. Exchange Rate Data

*   **Description**: Represents the current exchange rates fetched from an external API.
*   **Source**: External ExchangeRate-API.
*   **Attributes**:
    *   `base_currency`: (String) The currency against which all other rates are quoted (e.g., "USD").
    *   `conversion_rates`: (Dictionary) A mapping of target currency codes to their respective exchange rates against the base currency (e.g., `{"EUR": 0.92, "GBP": 0.79}`).
*   **Validation Rules**:
    *   API response must be successful.
    *   `conversion_rates` should contain valid currency codes and numerical rates.

### 3. Conversion Factors

*   **Description**: Static mappings of units to a common base unit for internal conversion logic.
*   **Types**: Weight, Length, Time.
*   **Attributes**:
    *   `unit_name`: (String) The name of the unit (e.g., "kg", "m", "hr").
    *   `factor_to_base`: (Float) The multiplier to convert this unit to its base unit (e.g., for "kg" to "g", factor is 1000).
*   **Relationships**: Used internally by `convert_weight.py`, `convert_length.py`, `convert_time.py`.

### 4. Calculation Result

*   **Description**: The output of any operation or conversion.
*   **Attributes**:
    *   `result`: (Float/Integer) The computed value.
    *   `unit`: (String, Optional) The unit of the result, if applicable (e.g., "EUR", "lb").
    *   `error`: (String, Optional) An error message if the operation failed.
*   **Validation Rules**:
    *   Result should be a valid number.
    *   Error message should be informative if present.
