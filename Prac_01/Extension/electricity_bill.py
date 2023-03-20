"""
CP1404 - Practice
Create an electricity bill estimator

Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75

Electricity bill estimator 2.0
Which tariff? 11 or 31: 11
Enter daily use in kWh: 13.4
Enter number of billing days: 90
Estimated bill: $295.01
"""

# Electricity bill estimator 1.0

INTRO = "Electricity bill estimator 1.0"

print(INTRO)
kwh_price = int(input("Enter cents per kWh: "))/100
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
total = kwh_price * daily_use * billing_days
print(f"Estimated bill ${total:,.2f}")


# Electricity bill estimator 2.0

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
INTRO = "Electricity bill estimator 2.0"
INVALID_MSG = "This is not a valid tariff"

print(INTRO)
tariff = int(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print(INVALID_MSG)
    tariff = float(input("Which tariff? 11 or 31: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_11
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
total = tariff * daily_use * billing_days
print(f"Estimated bill ${total:,.2f}")
