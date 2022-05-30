bought_food_kg = int(input())
bought_food_g = bought_food_kg * 1000
command_line = input()
sum_food_eaten_g = 0
is_food_enough = False
while command_line != "Adopted":
    food_eaten_in_g = int(command_line)
    sum_food_eaten_g += food_eaten_in_g

    if sum_food_eaten_g > bought_food_g:
        is_food_enough = False
    elif sum_food_eaten_g <= bought_food_g:
        is_food_enough = True
    command_line = input()

if is_food_enough == True:
    print(f"Food is enough! Leftovers: {bought_food_g-sum_food_eaten_g} grams." )
else:
    print(f"Food is not enough. You need {abs(sum_food_eaten_g - bought_food_g)} grams more." )