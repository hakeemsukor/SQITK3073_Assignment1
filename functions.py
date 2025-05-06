import csv
import pandas as pd

def verify_user(ic_number,password):
    return len(ic_number)==12 and password== ic_number[-4:]

def calculate_tax(income,tax_relief):
    chargeable_income= income-tax_relief
    if chargeable_income <= 0:
        return 0
    

    taxrate = [(5000, 0.00),
           (15000,0.01),
           (15000,0.03),
           (15000,0.06),
           (20000,0.11),
           (30000,0.19),
           (300000,0.25),
           (200000,0.26),
           (1400000,0.28),
           (float('inf'),0.30)
    ]

    tax = 0
    balance=chargeable_income
    for amount, rate in taxrate:
        if balance >0:
            taxable = min(balance, amount)
            tax += taxable*rate
            balance -= taxable
        else:
            break
    return round(tax, 2)

def save_to_csv(data, filename):
    file_exists = False

    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['IC Number', 'Income', 'Tax Relief', 'Tax Payable'])
        writer.writerow(data)

def read_from_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None

    


