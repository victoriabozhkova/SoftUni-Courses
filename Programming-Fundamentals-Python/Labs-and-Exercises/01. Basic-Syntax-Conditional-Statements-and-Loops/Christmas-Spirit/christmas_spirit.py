
quantity_of_decorations = int(input())
days_until_christmas = int(input())

money_spent = 0
spirit_points = 0

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

for i in range(1, days_until_christmas + 1):
    if i % 11 == 0:
        quantity_of_decorations += 2
    if i % 10 == 0:
        if days_until_christmas == i:
            spirit_points -= 30
        spirit_points -= 20
        money_spent += tree_skirt_price + tree_garland_price + tree_lights_price
    if i % 2 == 0:
        money_spent += quantity_of_decorations * ornament_set_price
        spirit_points += ornament_set_points
    if i % 3 == 0:
        money_spent += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        spirit_points += tree_skirt_points + tree_garland_points
    if i % 5 == 0:
        money_spent += tree_lights_price * quantity_of_decorations
        spirit_points += tree_lights_points
    if i % 3 == 0 and i % 5 == 0:
        spirit_points += 30


print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")








