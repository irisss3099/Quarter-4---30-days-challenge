import argparse
from calculator.math_ops import add, subtract, multiply, divide
from calculator.convert_currency import convert_currency
from calculator.convert_weight import convert_weight
from calculator.convert_length import convert_length
from calculator.convert_time import convert_time
from calculator.scientific_ops import sine, cosine, tangent, square_root, logarithm, power
from calculator.financial_ops import simple_interest, compound_interest, loan_payment

def main():
    parser = argparse.ArgumentParser(description="Advanced CLI Calculator")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Arithmetic parser
    arith_parser = subparsers.add_parser("arith", help="Basic arithmetic operations")
    arith_parser.add_argument("num1", type=float, help="First number")
    arith_parser.add_argument("operation", type=str, choices=["add", "sub", "mul", "div"], help="Operation (add, sub, mul, div)")
    arith_parser.add_argument("num2", type=float, help="Second number")

    # Currency conversion parser
    currency_parser = subparsers.add_parser("currency", help="Convert currencies")
    currency_parser.add_argument("amount", type=float, help="Amount to convert")
    currency_parser.add_argument("from_c", type=str, help="From currency (e.g., USD)")
    currency_parser.add_argument("to_c", type=str, help="To currency (e.g., EUR)")

    # Weight conversion parser
    weight_parser = subparsers.add_parser("weight", help="Convert weights")
    weight_parser.add_argument("value", type=float, help="Value to convert")
    weight_parser.add_argument("from_u", type=str, help="From unit (e.g., kg)")
    weight_parser.add_argument("to_u", type=str, help="To unit (e.g., lb)")

    # Length conversion parser
    length_parser = subparsers.add_parser("length", help="Convert lengths")
    length_parser.add_argument("value", type=float, help="Value to convert")
    length_parser.add_argument("from_u", type=str, help="From unit (e.g., m)")
    length_parser.add_argument("to_u", type=str, help="To unit (e.g., ft)")

    # Time conversion parser
    time_parser = subparsers.add_parser("time", help="Convert time units")
    time_parser.add_argument("value", type=float, help="Value to convert")
    time_parser.add_argument("from_u", type=str, help="From unit (e.g., s)")
    time_parser.add_argument("to_u", type=str, help="To unit (e.g., hr)")

    # Scientific functions parser
    scientific_parser = subparsers.add_parser("sci", help="Scientific functions")
    scientific_subparsers = scientific_parser.add_subparsers(dest="sci_op", help="Scientific operations")

    sine_parser = scientific_subparsers.add_parser("sin", help="Sine function")
    sine_parser.add_argument("angle", type=float, help="Angle in degrees")

    cos_parser = scientific_subparsers.add_parser("cos", help="Cosine function")
    cos_parser.add_argument("angle", type=float, help="Angle in degrees")

    tan_parser = scientific_subparsers.add_parser("tan", help="Tangent function")
    tan_parser.add_argument("angle", type=float, help="Angle in degrees")

    sqrt_parser = scientific_subparsers.add_parser("sqrt", help="Square root function")
    sqrt_parser.add_argument("number", type=float, help="Number")

    log_parser = scientific_subparsers.add_parser("log", help="Logarithm function (base 10)")
    log_parser.add_argument("number", type=float, help="Number")

    pow_parser = scientific_subparsers.add_parser("pow", help="Power function")
    pow_parser.add_argument("base", type=float, help="Base")
    pow_parser.add_argument("exponent", type=float, help="Exponent")

    # Financial functions parser
    financial_parser = subparsers.add_parser("fin", help="Financial calculations")
    financial_subparsers = financial_parser.add_subparsers(dest="fin_op", help="Financial operations")

    si_parser = financial_subparsers.add_parser("si", help="Simple Interest")
    si_parser.add_argument("principal", type=float, help="Principal amount")
    si_parser.add_argument("rate", type=float, help="Annual interest rate (e.g., 0.05 for 5%)")
    si_parser.add_argument("time", type=float, help="Time in years")

    ci_parser = financial_subparsers.add_parser("ci", help="Compound Interest")
    ci_parser.add_argument("principal", type=float, help="Principal amount")
    ci_parser.add_argument("rate", type=float, help="Annual interest rate (e.g., 0.05 for 5%)")
    ci_parser.add_argument("time", type=float, help="Time in years")
    ci_parser.add_argument("n", type=int, help="Number of times interest is compounded per year")

    lp_parser = financial_subparsers.add_parser("lp", help="Loan Payment")
    lp_parser.add_argument("principal", type=float, help="Principal loan amount")
    lp_parser.add_argument("annual_rate", type=float, help="Annual interest rate (e.g., 0.05 for 5%)")
    lp_parser.add_argument("loan_term", type=float, help="Loan term in years")

    args = parser.parse_args()

    try:
        if args.command == "arith":
            if args.operation == "add":
                result = add(args.num1, args.num2)
            elif args.operation == "sub":
                result = subtract(args.num1, args.num2)
            elif args.operation == "mul":
                result = multiply(args.num1, args.num2)
            elif args.operation == "div":
                result = divide(args.num1, args.num2)
            print(f"Result: {result}")
        elif args.command == "currency":
            converted_amount = convert_currency(args.amount, args.from_c.upper(), args.to_c.upper())
            if converted_amount is not None:
                print(f"{args.amount} {args.from_c.upper()} is {converted_amount:.2f} {args.to_c.upper()}")
            else:
                print("Could not fetch exchange rates. Please check your API key or network connection.")
        elif args.command == "weight":
            converted_value = convert_weight(args.value, args.from_u.lower(), args.to_u.lower())
            print(f"{args.value} {args.from_u.lower()} is {converted_value:.2f} {args.to_u.lower()}")
        elif args.command == "length":
            converted_value = convert_length(args.value, args.from_u.lower(), args.to_u.lower())
            print(f"{args.value} {args.from_u.lower()} is {converted_value:.2f} {args.to_u.lower()}")
        elif args.command == "time":
            converted_value = convert_time(args.value, args.from_u.lower(), args.to_u.lower())
            print(f"{args.value} {args.from_u.lower()} is {converted_value:.2f} {args.to_u.lower()}")
        elif args.command == "sci":
            if args.sci_op == "sin":
                result = sine(args.angle)
            elif args.sci_op == "cos":
                result = cosine(args.angle)
            elif args.sci_op == "tan":
                result = tangent(args.angle)
            elif args.sci_op == "sqrt":
                result = square_root(args.number)
            elif args.sci_op == "log":
                result = logarithm(args.number)
            elif args.sci_op == "pow":
                result = power(args.base, args.exponent)
            print(f"Result: {result}")
        elif args.command == "fin":
            if args.fin_op == "si":
                result = simple_interest(args.principal, args.rate, args.time)
            elif args.fin_op == "ci":
                result = compound_interest(args.principal, args.rate, args.time, args.n)
            elif args.fin_op == "lp":
                result = loan_payment(args.principal, args.annual_rate, args.loan_term)
            print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        parser.print_help()

if __name__ == "__main__":
    main()
