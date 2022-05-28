city = input()
type_of_package = input()
vip = input()
days = int(input())
price_per_day = 0
if city == "Bansko" or city == "Borovets":
    if type_of_package == "withEquipment":
        price_per_day = 100
        if vip == "yes":
            price_per_day = price_per_day * 0.9
    elif type_of_package == "noEquipment":
        price_per_day = 80
        if vip == "yes":
            price_per_day = price_per_day * 0.95
elif city == "Varna" or city == "Burgas":
    if type_of_package == "withBreakfast":
        price_per_day = 130
        if vip == "yes":
            price_per_day = price_per_day * 0.88
    elif type_of_package == "noBreakfast":
        price_per_day = 100
        if vip == "yes":
            price_per_day = price_per_day * 0.93
sum_price = days * price_per_day
if days >= 7:
    sum_price = sum_price - price_per_day

if days < 1:
    print("Days must be positive number!")
elif city != "Bansko" and city != "Borovets" and city != "Varna" and city != "Burgas":
    print("Invalid input!")
elif type_of_package != "noEquipment" and type_of_package != "withEquipment" and type_of_package != "noBreakfast" and type_of_package != "withBreakfast":
    print("Invalid input!")
else:
    print(f"The price is {sum_price:.2f}lv! Have a nice time!")