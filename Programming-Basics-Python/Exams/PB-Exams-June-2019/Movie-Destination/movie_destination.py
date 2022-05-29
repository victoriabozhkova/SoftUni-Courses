budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    elif destination == "London":
        price_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    elif destination == "London":
        price_per_day = 20250

final_price = days * price_per_day

if destination == "Dubai":
    final_price = final_price * 0.7
elif destination == "Sofia":
    final_price = final_price * 1.25

if final_price > budget:
    print(f"The director needs {final_price - budget:.2f} leva more!")
else:
    print(f"The budget for the movie is enough! We have {budget - final_price:.2f} leva left!")
