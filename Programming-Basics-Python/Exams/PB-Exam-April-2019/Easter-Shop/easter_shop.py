initial_egg_sum = int(input())
egg_sum = initial_egg_sum

command_line = input()

are_eggs_not_enough= False
bought_eggs = 0
while command_line != "Close":
    action = command_line
    egg_quantity = int(input())
    if action == "Buy":
        bought_eggs += egg_quantity
        if egg_quantity > egg_sum:
            are_eggs_not_enough = True
            break
        else:
            egg_sum -= egg_quantity
    elif action == "Fill":
        egg_sum += egg_quantity

    command_line = input()

if are_eggs_not_enough:
    print("Not enough eggs in store!")
    print(f"You can buy only {egg_sum}.")
else:
    print(f"Store is closed!")
    print(f"{bought_eggs} eggs sold.")