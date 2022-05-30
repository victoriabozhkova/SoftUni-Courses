days = int(input())
init_food = float(input())
biscuits = 0
dog_food = 0
cat_food = 0

for i in range(1, days+1):
    food_per_day = 0
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    food_per_day = dog_food_eaten + cat_food_eaten

    if i % 3 == 0:
        biscuits += food_per_day * 0.1

    dog_food += dog_food_eaten
    cat_food += cat_food_eaten

sum_food_eaten = dog_food + cat_food

sum_food_eaten_percent = sum_food_eaten / init_food  * 100
dog_food_eaten_percent = dog_food / sum_food_eaten  * 100
cat_food_eaten_percent = cat_food / sum_food_eaten * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{sum_food_eaten_percent:.2f}% of the food has been eaten.")
print(f"{dog_food_eaten_percent:.2f}% eaten from the dog.")
print(f"{cat_food_eaten_percent:.2f}% eaten from the cat.")
