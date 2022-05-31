budget = float(input())
needed_fuel= float(input())
day_of_the_week = input()

litre_of_gas_price = 2.1
gid_price = 100

final_price = needed_fuel * litre_of_gas_price + gid_price

if day_of_the_week == "Saturday":
    final_price = final_price * 0.9
elif day_of_the_week == "Sunday":
    final_price = final_price * 0.8

if final_price <= budget:
    print(f"Safari time! Money left: {budget - final_price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(budget-final_price):.2f} lv.")