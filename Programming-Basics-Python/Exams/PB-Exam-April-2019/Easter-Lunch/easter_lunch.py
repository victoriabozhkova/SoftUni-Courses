cakes_sum = int(input())
eggs_carton_sum = int(input())
cookies_kg = int(input())
sum_eggs = eggs_carton_sum * 12
cake_price = 3.2
eggs_price_12 = 4.35
cookies_price = 5.4
egg_dye = 0.15

sum_price = cake_price * cakes_sum + eggs_carton_sum * eggs_price_12 + cookies_kg * cookies_price + egg_dye * sum_eggs

print(f"{sum_price:.2f}")
