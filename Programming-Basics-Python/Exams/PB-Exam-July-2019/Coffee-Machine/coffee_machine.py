type_of_drink = input()
sugar = input()
number_of_drinks = int(input())
price = 0

if type_of_drink == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif type_of_drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif type_of_drink == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7
sum_price = price * number_of_drinks

if sugar == "Without":
    sum_price = sum_price * 0.65
if type_of_drink == "Espresso" and number_of_drinks >= 5:
    sum_price = sum_price * 0.75
if sum_price > 15:
    sum_price = sum_price * 0.80


print(f"You bought {number_of_drinks} cups of {type_of_drink} for {sum_price:.2f} lv.")
