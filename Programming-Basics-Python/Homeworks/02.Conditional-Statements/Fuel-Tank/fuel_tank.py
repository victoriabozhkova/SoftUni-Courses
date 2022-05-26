fuel = input()
fuel_in_tank = float(input())


if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if fuel_in_tank >= 25:
        print(f"You have enough {fuel.lower()}.")
    elif fuel_in_tank < 25:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")


