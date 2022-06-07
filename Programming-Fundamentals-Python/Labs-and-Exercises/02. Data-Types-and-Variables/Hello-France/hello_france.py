items = input().split("|")
budget = int(input())
budget_left = budget
bought_items_prices = []

for item in items:
    new_list_items = item.split("->")
    item_to_buy = new_list_items[0]
    price = float(new_list_items[1])
    price_is_valid = False

    if price > budget_left:
        continue

    if item_to_buy == "Clothes":
        if price > 50.00:
            continue
        else:
            price_is_valid = True
    elif item_to_buy == "Shoes":
        if price > 35.00:
            continue
        else:
            price_is_valid = True
    elif item_to_buy == "Accessories":
        if price > 20.50:
            continue
        else:
            price_is_valid = True

    if price_is_valid:
        budget_left -= price
        bought_items_prices.append(price)

new_prices = []
final_money = 0
profit = 0

for bought_item_price in bought_items_prices:
    price_with_markup = bought_item_price * 1.4
    profit += price_with_markup - bought_item_price
    new_prices.append(price_with_markup)
    print(f"{price_with_markup:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
final_money = budget + profit
if final_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")






