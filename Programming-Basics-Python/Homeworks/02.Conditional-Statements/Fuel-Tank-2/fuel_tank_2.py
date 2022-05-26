fuel = input()
sum_fuel = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
final_price = 0

if fuel == "Gas":
    final_price = gas_price * sum_fuel
    if club_card == "Yes":
        final_price -= 0.08 * sum_fuel
elif fuel == "Gasoline":
    final_price = gasoline_price * sum_fuel
    if club_card == "Yes":
        final_price -= 0.18 * sum_fuel
elif fuel == "Diesel":
    final_price = diesel_price * sum_fuel
    if club_card == "Yes":
        final_price -= 0.12 * sum_fuel

if 20 <= sum_fuel <= 25:
    final_price = final_price * 0.92
elif sum_fuel > 25:
    final_price = final_price * 0.9

print(f"{final_price:.2f} lv.")