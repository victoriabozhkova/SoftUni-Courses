size_of_the_eggs = input()
color_of_the_eggs = input()
batches_sum = int(input())
price  = 0

if size_of_the_eggs == "Large":
    if color_of_the_eggs == "Red":
        price = 16
    elif color_of_the_eggs == "Green":
        price = 12
    elif color_of_the_eggs == "Yellow":
        price = 9
elif size_of_the_eggs == "Medium":
    if color_of_the_eggs == "Red":
        price = 13
    elif color_of_the_eggs == "Green":
        price = 9
    elif color_of_the_eggs == "Yellow":
        price = 7
elif size_of_the_eggs == "Small":
    if color_of_the_eggs == "Red":
        price = 9
    elif color_of_the_eggs == "Green":
        price = 8
    elif color_of_the_eggs == "Yellow":
        price = 5

eggs_price = batches_sum * price
final_price = eggs_price - eggs_price * 0.35

print(f"{final_price:.2f} leva.")

