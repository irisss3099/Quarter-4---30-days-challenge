# Advanced CLI & Streamlit Calculator

This project implements an advanced calculator with both a Command-Line Interface (CLI) and an interactive Streamlit web application. It supports basic arithmetic, various unit conversions (currency, weight, length, time), scientific functions, and financial calculations.

## Features

*   **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
*   **Currency Conversion:** Live exchange rate conversion using the ExchangeRate-API.
*   **Unit Conversions:**
    *   **Weight:** Kilograms, grams, milligrams, pounds, ounces.
    *   **Length:** Meters, centimeters, kilometers, inches, feet, yards, miles.
    *   **Time:** Seconds, minutes, hours, days, weeks.
*   **Scientific Functions:** Sine, cosine, tangent, square root, logarithm, power.
*   **Financial Calculations:** Simple interest, compound interest, loan payment.
*   **User Interfaces:**
    *   **Command-Line Interface (CLI):** For quick calculations directly from the terminal.
    *   **Streamlit Web Application:** An interactive and animated graphical user interface.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd advanced_calculator
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Key for Currency Conversion:**
    The currency conversion feature requires an API key from [ExchangeRate-API](https://www.exchangerate-api.com/).
    *   Sign up and get your API key.
    *   Set it as an environment variable named `EXCHANGE_RATE_API_KEY`.
        *   **Windows:**
            ```bash
            set EXCHANGE_RATE_API_KEY=YOUR_API_KEY
            ```
        *   **macOS/Linux:**
            ```bash
            export EXCHANGE_RATE_API_KEY=YOUR_API_KEY
            ```
        (Replace `YOUR_API_KEY` with your actual key.)

## Usage

### Command-Line Interface (CLI)

Run `cli_main.py` with the desired command and arguments.

*   **Arithmetic:**
    ```bash
    python cli_main.py arith 10 add 5
    python cli_main.py arith 10 mul 2.5
    ```

*   **Currency Conversion:**
    ```bash
    python cli_main.py currency 100 USD EUR
    ```
    (Ensure `EXCHANGE_RATE_API_KEY` is set)

*   **Weight Conversion:**
    ```bash
    python cli_main.py weight 5 kg lb
    ```

*   **Length Conversion:**
    ```bash
    python cli_main.py length 10 m ft
    ```

*   **Time Conversion:**
    ```bash
    python cli_main.py time 3600 s hr
    ```

*   **Scientific Functions:**
    ```bash
    python cli_main.py sci sin 90
    python cli_main.py sci sqrt 25
    python cli_main.py sci log 100
    python cli_main.py sci pow 2 3
    ```

*   **Financial Calculations:**
    *   **Simple Interest:**
        ```bash
        python cli_main.py fin si 1000 0.05 2
        ```
    *   **Compound Interest:**
        ```bash
        python cli_main.py fin ci 1000 0.05 2 12
        ```
    *   **Loan Payment:**
        ```bash
        python cli_main.py fin lp 100000 0.04 30
        ```

### Streamlit Web Application

To run the interactive UI, navigate to the project root and execute:

```bash
streamlit run app.py
```

This will open the calculator in your web browser.

## Project Structure

```
.
├── calculator/
│   ├── __init__.py
│   ├── math_ops.py             # Basic arithmetic operations
│   ├── convert_currency.py     # Currency conversion (API integration)
│   ├── convert_weight.py       # Weight unit conversion
│   ├── convert_length.py       # Length unit conversion
│   ├── convert_time.py         # Time unit conversion
│   ├── scientific_ops.py       # Scientific functions (sine, cosine, etc.)
│   ├── financial_ops.py        # Financial calculations (interest, loan payment)
│   └── utils.py                # Utility functions (validation)
├── app.py                      # Streamlit web application
├── cli_main.py                 # Command-line interface
└── requirements.txt            # Python dependencies
```

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is open-source and available under the MIT License.
