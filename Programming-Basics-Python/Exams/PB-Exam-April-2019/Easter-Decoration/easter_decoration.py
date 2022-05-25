clients_number = int(input())

price = 0
price_sum = 0
for i in range(1, clients_number + 1):
    command_line = input()
    final_price_for_client = 0
    product_count = 0
    while command_line != "Finish":
        product = command_line
        product_count += 1
        if product == "basket":
            price = 1.5
        elif product == "wreath":
            price = 3.8
        elif product == "chocolate bunny":
            price = 7

        final_price_for_client += price

        command_line = input()
    if product_count % 2 == 0:
        final_price_for_client = final_price_for_client * 0.8
    price_sum += final_price_for_client
    print(f"You purchased {product_count} items for {final_price_for_client:.2f} leva.")

avg_price = price_sum / clients_number
print(f"Average bill per client is: {avg_price:.2f} leva.")
