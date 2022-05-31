contract_time = input()
type_contract = input()
included_internet = input()
months_payment = int(input())

price_per_month = 0

if type_contract == "Small":
    if contract_time == "one":
        price_per_month = 9.98
    elif contract_time == "two":
        price_per_month = 8.58
elif type_contract == "Middle":
    if contract_time == "one":
        price_per_month = 18.99
    elif contract_time == "two":
        price_per_month = 17.09
elif type_contract == "Large":
    if contract_time == "one":
        price_per_month = 25.98
    elif contract_time == "two":
        price_per_month = 23.59
elif type_contract == "ExtraLarge":
    if contract_time == "one":
        price_per_month = 35.99
    elif contract_time == "two":
        price_per_month = 31.79

if included_internet == "yes":
    if price_per_month <= 10:
        price_per_month += 5.5
    elif price_per_month <= 30:
        price_per_month += 4.35
    elif price_per_month > 30:
        price_per_month += 3.85

final_price = price_per_month * months_payment

if contract_time == "two":
    final_price = final_price * (1 - 0.0375)

print(f"{final_price:.2f} lv.")

