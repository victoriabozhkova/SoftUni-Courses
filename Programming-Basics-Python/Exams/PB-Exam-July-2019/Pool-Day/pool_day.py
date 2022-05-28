people = int(input())
entrance_price = float(input())
sunbed_price = float(input())
umbrella_price = float(input())
import math
entrance_price_for_all = people * entrance_price

sunbeds_count = math.ceil(0.75 * people)
umbrellas_count = math.ceil(people/2)

sunbed_price_for_all = sunbeds_count * sunbed_price
umbrella_price_for_all = umbrellas_count *umbrella_price
sum_price = entrance_price_for_all + sunbed_price_for_all + umbrella_price_for_all

print(f"{sum_price:.2f} lv.")