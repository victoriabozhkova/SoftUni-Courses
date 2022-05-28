profit_target = float(input())
command = input()
profit = 0
order_price = 0
while command != "Party!":
    cocktail_name = command
    number_of_cocktails = int(input())

    cocktail_price = len(cocktail_name)
    order_price = cocktail_price * number_of_cocktails

    if order_price % 2 == 1:
        order_price = order_price * 0.75

    profit = profit + order_price

    if command == "Party!":
        break

    if profit >= profit_target:
        break

    command = input()

if command == "Party!":
    print(f"We need {profit_target - profit:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {profit:.2f} leva.")







