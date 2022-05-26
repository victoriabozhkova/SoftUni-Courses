vineyard_area = int(input())
grape_sq_m = float(input())
needed_wine_l = int(input())
workers = int(input())

kg_grape = vineyard_area * grape_sq_m
harvest_for_wine = kg_grape * 0.4
wine_l = harvest_for_wine / 2.5

import math
if wine_l >= needed_wine_l:
    wine_per_worker = (wine_l - needed_wine_l) / workers
    print(f"Good harvest this year! Total wine: {math.floor(abs(wine_l))} liters.")
    print(f"{math.ceil(abs(wine_l - needed_wine_l))} liters left -> {math.ceil(abs(wine_per_worker))} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(abs(needed_wine_l - wine_l))} liters wine needed.")
