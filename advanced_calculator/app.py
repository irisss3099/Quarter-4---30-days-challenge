import streamlit as st
from calculator.math_ops import add, subtract, multiply, divide
from calculator.convert_currency import convert_currency
from calculator.convert_weight import convert_weight
from calculator.convert_length import convert_length
from calculator.convert_time import convert_time
from calculator.scientific_ops import sine, cosine, tangent, square_root, logarithm, power
from calculator.financial_ops import simple_interest, compound_interest, loan_payment

st.set_page_config(layout="wide")

st.title("Advanced Calculator")

# Sidebar for navigation
menu = st.sidebar.selectbox("Select Calculator Type", ("Arithmetic", "Scientific Functions", "Financial Calculations", "Currency Converter", "Weight Converter", "Length Converter", "Time Converter"))

if menu == "Arithmetic":
    st.header("Basic Arithmetic")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, key="arith_num1")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, key="arith_num2")

    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    result = None
    if st.button("Calculate Arithmetic"):
        try:
            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(f"Error: {e}")

elif menu == "Scientific Functions":
    st.header("Scientific Functions")

    operation = st.selectbox("Select operation", ("Sine (degrees)", "Cosine (degrees)", "Tangent (degrees)", "Square Root", "Logarithm (base 10)", "Power"))

    if operation in ("Sine (degrees)", "Cosine (degrees)", "Tangent (degrees)", "Square Root", "Logarithm (base 10)"):
        num = st.number_input("Enter number", value=0.0, key="sci_num")
        if st.button(f"Calculate {operation}"):
            try:
                if operation == "Sine (degrees)":
                    result = sine(num)
                elif operation == "Cosine (degrees)":
                    result = cosine(num)
                elif operation == "Tangent (degrees)":
                    result = tangent(num)
                elif operation == "Square Root":
                    result = square_root(num)
                elif operation == "Logarithm (base 10)":
                    result = logarithm(num)
                st.success(f"Result: {result}")
            except ValueError as e:
                st.error(f"Error: {e}")
    elif operation == "Power":
        base = st.number_input("Enter base", value=0.0, key="sci_base")
        exponent = st.number_input("Enter exponent", value=0.0, key="sci_exponent")
        if st.button("Calculate Power"):
            try:
                result = power(base, exponent)
                st.success(f"Result: {result}")
            except ValueError as e:
                st.error(f"Error: {e}")

elif menu == "Financial Calculations":
    st.header("Financial Calculations")

    operation = st.selectbox("Select operation", ("Simple Interest", "Compound Interest", "Loan Payment"))

    if operation == "Simple Interest":
        principal_si = st.number_input("Principal Amount", value=1000.0, key="principal_si")
        rate_si = st.number_input("Annual Interest Rate (e.g., 0.05 for 5%)", value=0.05, key="rate_si")
        time_si = st.number_input("Time (years)", value=1.0, key="time_si")
        if st.button("Calculate Simple Interest"):
            try:
                result = simple_interest(principal_si, rate_si, time_si)
                st.success(f"Simple Interest: {result:.2f}")
            except ValueError as e:
                st.error(f"Error: {e}")

    elif operation == "Compound Interest":
        principal_ci = st.number_input("Principal Amount", value=1000.0, key="principal_ci")
        rate_ci = st.number_input("Annual Interest Rate (e.g., 0.05 for 5%)", value=0.05, key="rate_ci")
        time_ci = st.number_input("Time (years)", value=1.0, key="time_ci")
        n_ci = st.number_input("Number of times interest is compounded per year", value=1, step=1, key="n_ci")
        if st.button("Calculate Compound Interest"):
            try:
                result = compound_interest(principal_ci, rate_ci, time_ci, n_ci)
                st.success(f"Compound Interest: {result:.2f}")
            except ValueError as e:
                st.error(f"Error: {e}")

    elif operation == "Loan Payment":
        principal_lp = st.number_input("Principal Loan Amount", value=10000.0, key="principal_lp")
        annual_rate_lp = st.number_input("Annual Interest Rate (e.g., 0.05 for 5%)", value=0.05, key="annual_rate_lp")
        loan_term_lp = st.number_input("Loan Term (years)", value=5, step=1, key="loan_term_lp")
        if st.button("Calculate Loan Payment"):
            try:
                result = loan_payment(principal_lp, annual_rate_lp, loan_term_lp)
                st.success(f"Monthly Loan Payment: {result:.2f}")
            except ValueError as e:
                st.error(f"Error: {e}")

elif menu == "Currency Converter":
    st.header("Currency Converter")

    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount", value=1.0, key="currency_amount")
    with col2:
        from_currency = st.text_input("From Currency (e.g., USD)", "USD", key="from_currency").upper()
        to_currency = st.text_input("To Currency (e.g., EUR)", "EUR", key="to_currency").upper()

    if st.button("Convert Currency"):
        try:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                st.success(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
            else:
                st.warning("Could not fetch exchange rates. Please check your API key or network connection.")
        except ValueError as e:
            st.error(f"Error: {e}")

elif menu == "Weight Converter":
    st.header("Weight Converter")

    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Value", value=0.0, key="weight_value")
    with col2:
        from_unit = st.text_input("From Unit (e.g., kg)", "kg", key="from_weight_unit").lower()
        to_unit = st.text_input("To Unit (e.g., lb)", "lb", key="to_weight_unit").lower()

    if st.button("Convert Weight"):
        try:
            converted_value = convert_weight(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is {converted_value:.2f} {to_unit}")
        except ValueError as e:
            st.error(f"Error: {e}")

elif menu == "Length Converter":
    st.header("Length Converter")

    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Value", value=0.0, key="length_value")
    with col2:
        from_unit = st.text_input("From Unit (e.g., m)", "m", key="from_length_unit").lower()
        to_unit = st.text_input("To Unit (e.g., ft)", "ft", key="to_length_unit").lower()

    if st.button("Convert Length"):
        try:
            converted_value = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is {converted_value:.2f} {to_unit}")
        except ValueError as e:
            st.error(f"Error: {e}")

elif menu == "Time Converter":
    st.header("Time Converter")

    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Value", value=0.0, key="time_value")
    with col2:
        from_unit = st.text_input("From Unit (e.g., s)", "s", key="from_time_unit").lower()
        to_unit = st.text_input("To Unit (e.g., hr)", "hr", key="to_time_unit").lower()

    if st.button("Convert Time"):
        try:
            converted_value = convert_time(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is {converted_value:.2f} {to_unit}")
        except ValueError as e:
            st.error(f"Error: {e}")
