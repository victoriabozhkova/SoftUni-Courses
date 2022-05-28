import math

wall_height = int(input())
wall_width = int(input())
percent_not_painted = int(input())
wall_area = wall_width * wall_height * 4
area_to_paint = wall_area * (100 - percent_not_painted) / 100
walls_are_painted= False
sum_paint = 0
command_line = input()
while command_line != "Tired!":
    paint_litres = int(command_line)
    sum_paint += paint_litres
    area_to_paint -= paint_litres
    if area_to_paint <= 0:
        walls_are_painted = True
        break
    command_line = input()

if walls_are_painted and area_to_paint == 0:
    print("All walls are painted! Great job, Pesho!")
elif walls_are_painted and sum_paint > area_to_paint:
    print(f"All walls are painted and you have {math.ceil(abs(area_to_paint))} l paint left!")
elif area_to_paint > sum_paint:
    print(f"{math.ceil(area_to_paint)} quadratic m left.")

