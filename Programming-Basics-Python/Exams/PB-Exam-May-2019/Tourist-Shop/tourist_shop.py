budget = float(input())
budget_left = budget
command_line = input()
position = 0
is_budget_not_left = False

while command_line != "Stop":
    product_name = command_line
    product_price = float(input())
    position += 1
    if position % 3 == 0:
        product_price /= 2

    if product_price > budget_left:
        is_budget_not_left = True
        break

    budget_left -= product_price

    command_line = input()

if is_budget_not_left:
    print(f"You don't have enough money!")
    print(f"You need {abs(product_price - budget_left):.2f} leva!")
else:
    print(f"You bought {position} products for {budget - budget_left:.2f} leva.")






