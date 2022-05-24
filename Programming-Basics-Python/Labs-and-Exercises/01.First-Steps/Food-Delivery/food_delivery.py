chicken_menus = int(input())
fish_menus = int(input())
veg_menus = int(input())

price_chicken_menus = chicken_menus * 10.35
price_fish_menus = fish_menus * 12.4
price_veg_menus = veg_menus * 8.15
price_dessert = (price_veg_menus + price_fish_menus + price_chicken_menus) * 0.2

final_price = price_dessert + price_fish_menus + price_chicken_menus + price_veg_menus + 2.5

print(final_price)
