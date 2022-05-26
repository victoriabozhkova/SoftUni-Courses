days = int(input())
food_init = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food_in_g = float(input())

turtle_food_in_kg = turtle_food_in_g / 1000

sum_food_eaten = days * (dog_food + cat_food + turtle_food_in_kg)
import math
if sum_food_eaten <= food_init:
    print(f"{math.floor(food_init - sum_food_eaten)} kilos of food left.")
else:
    print(f"{math.ceil(abs(food_init - sum_food_eaten))} more kilos of food are needed.")

