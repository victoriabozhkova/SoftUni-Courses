budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percent = int(input())

if nights > 7:
    price_per_night = price_per_night * 0.95

additional_expenses = budget * (additional_expenses_percent / 100)

price_nights_sum = price_per_night * nights

final_sum = price_nights_sum + additional_expenses

if final_sum <= budget:
    print(f"Ivanovi will be left with {budget-final_sum:.2f} leva after vacation.")
else:
    print(f"{abs(budget-final_sum):.2f} leva needed.")