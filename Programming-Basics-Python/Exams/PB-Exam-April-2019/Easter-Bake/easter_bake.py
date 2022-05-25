number_of_cakes = int(input())
import sys
max_sugar_used = - sys.maxsize
max_flour_used = - sys.maxsize

sugar_count = 0
flour_count = 0

for i in range(0, number_of_cakes):
    sugar_used = int(input())
    flour_used = int(input())

    sugar_count += sugar_used
    flour_count += flour_used


    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used


sugar_packs = sugar_count / 950
flour_packs = flour_count / 750

import math
print(f"Sugar: {math.ceil(sugar_packs)}")
print(f"Flour: {math.ceil(flour_packs)}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
