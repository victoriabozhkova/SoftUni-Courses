guests = int(input())
budget = int(input())
import math

cakes_count= math.ceil(guests / 3)
eggs_count = guests * 2

cake_price = 4
egg_price = 0.45

final_price = cake_price * cakes_count + egg_price * eggs_count

if final_price > budget:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(final_price-budget):.2f} lv. more.")
elif final_price <= budget:
    print(f"Lyubo bought {cakes_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {budget-final_price:.2f} lv. left.")
