budget = float(input())
extras = int(input())
clothes_per_extra = float(input())

if extras > 150:
    clothes_per_extra *= 0.9

sum_price_clothes = extras * clothes_per_extra

decor_price = budget * 0.1

sum_price = sum_price_clothes + decor_price

if sum_price <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {abs(sum_price-budget):.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {abs(sum_price-budget):.2f} leva more.")