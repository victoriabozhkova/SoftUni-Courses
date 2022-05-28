bags_over_20_kg = float(input())
kg_bags = float(input())
days_holiday = int(input())
number_of_bags = int(input())

price = 0

if kg_bags < 10:
    price = bags_over_20_kg * 0.2
elif 10 <= kg_bags <= 20:
    price = bags_over_20_kg * 0.5
elif kg_bags > 20:
    price = bags_over_20_kg

if days_holiday > 30:
    price = price * 1.1
elif 30 >= days_holiday >= 7:
    price = price * 1.15
elif days_holiday < 7:
    price = price * 1.4

final_price = price * number_of_bags

print(f"The total price of bags is: {final_price:.2f} lv. ")
