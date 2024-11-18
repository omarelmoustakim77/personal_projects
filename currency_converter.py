import sys

rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "CAD": 1.35,
    "JPY": 110.0,
    "GBP": 0.75,
    "AUD": 1.5,
    "CHF": 0.91,
    "CNY": 6.45,
    "INR": 82.0,
    "ZAR": 18.0,
    "MXN": 19.8,
    "BRL": 5.2,
    "KRW": 1315.0
}

def display_menu():
    print("\n🌎 Welcome to the Advanced Currency Converter 🌎")
    print("Available Currencies:")
    for currency, rate in rates.items():
        print(f" - {currency} (1 {currency} = {rate:.2f} USD)")
    print("\nType 'exit' to quit the program.\n")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            return amount
        except ValueError as e:
            print(f"Invalid input. {e}")

def get_currency(prompt):
    while True:
        currency = input(prompt).upper()
        if currency == 'EXIT':
            sys.exit("Goodbye!")
        elif currency in rates:
            return currency
        else:
            print("Currency not supported. Please choose from the list.")

def currency_converter():
    while True:
        display_menu()
        
        from_currency = get_currency("Convert from (e.g., USD): ")

        amount = get_amount()

        to_currency = input("Convert to (or type 'custom' to add a custom rate): ").upper()
        if to_currency == "CUSTOM":
            custom_rate = float(input("Enter the exchange rate to your custom currency: "))
            converted = amount * custom_rate
            print(f"\n💹 {amount:.2f} {from_currency} = {converted:.2f} (custom rate: {custom_rate:.2f})\n")
        elif to_currency in rates:
            
            converted = amount * (rates[to_currency] / rates[from_currency])
            print(f"\n💹 {amount:.2f} {from_currency} = {converted:.2f} {to_currency}\n")
        else:
            print("Currency not supported. Please try again.\n")

        repeat = input("Would you like to convert another currency? (yes/no): ").lower()
        if repeat != "yes":
            print("Thank you for using the Currency Converter. Goodbye!")
            break

currency_converter()
