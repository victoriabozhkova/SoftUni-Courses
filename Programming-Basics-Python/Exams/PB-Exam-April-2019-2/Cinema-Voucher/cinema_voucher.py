voucher_value = int(input())

money_left = voucher_value
movie_counter = 0
other_purchases = 0

command = input()
while command != "End":
    purchase = command
    price = 0
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > money_left:
            break
        movie_counter += 1
    elif len(purchase) <= 8:
        price = ord(purchase[0])
        if price > money_left:
            break
        other_purchases += 1

    money_left -= price
    command = input()

print(movie_counter)
print(other_purchases)








