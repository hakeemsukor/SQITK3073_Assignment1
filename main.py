import functions as fx

FILENAME = 'tax_data.csv'

def main():
    print("Welcome to tax calculator")

    while True:
        ic = input("Enter your IC number: ")
        while len(ic) != 12:
            ic = input("Invalid IC number! Enter 12-digit IC number: ")

        password = input("Enter your password: ")

        if fx.verify_user(ic, password):
            print("Login successful.\n")
            break
        else:
            print("Login failed. Try again.\n")

    income = float(input("Enter your annual income (RM): "))

    print("You may be eligible for the following tax reliefs:")
    print("Individual relief: RM9,000")
    print("Spouse relief: RM4,000 (if spouse earns less than RM4,000/year)")
    print("Child relief: RM8,000 per child (up to 12 children)")
    print("Medical expenses: Up to RM8,000")
    print("Lifestyle expenses: Up to RM2,500")
    print("Education fees: Up to RM7,000")
    print("Parental care: Up to RM5,000")

    tax_relief = float(input("Enter your total tax relief (RM): "))

    tax = fx.calculate_tax(income, tax_relief)
    print(f"Your tax payable is: RM {tax:.2f}")

    fx.save_to_csv([ic, income, tax_relief, tax], FILENAME)
    print("Data saved to file.")

    print("Previous Tax Records")
    df = fx.read_from_csv(FILENAME)
    if df is not None:
        print(df)
    else:
        print("No previous records")

if __name__ == "__main__":
    main()
