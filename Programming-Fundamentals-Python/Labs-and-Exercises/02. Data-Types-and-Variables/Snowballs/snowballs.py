import sys

number_of_snowballs = int(input())
max_points = -sys.maxsize
for snowball in range(1, number_of_snowballs + 1):
    value = 0
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_points:
        max_points = value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(max_points)} ({snowball_quality})")


