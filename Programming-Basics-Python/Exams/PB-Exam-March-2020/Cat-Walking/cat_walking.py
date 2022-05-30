min_walk_per_day = int(input())
number_of_walks = int(input())
taken_calories_per_day = int(input())

sum_calories_burned = min_walk_per_day * number_of_walks * 5


if sum_calories_burned >= taken_calories_per_day /2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {sum_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {sum_calories_burned}.")

