months = int(input())
electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bills = 0
all_bills = 0
for i in range(1, months + 1):
    electricity_bill_per_month = float(input())
    water_bill_per_month = 20
    internet_bill_per_month = 15
    other_bills_per_month =electricity_bill_per_month + water_bill_per_month + internet_bill_per_month + (electricity_bill_per_month + water_bill_per_month + internet_bill_per_month) * 0.2

    electricity_bill = electricity_bill + electricity_bill_per_month
    water_bill = water_bill + water_bill_per_month
    internet_bill = internet_bill + internet_bill_per_month
    other_bills = other_bills + other_bills_per_month

    all_bills = all_bills + electricity_bill_per_month + water_bill_per_month + internet_bill_per_month + other_bills_per_month

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {all_bills/months:.2f} lv")

