fruit = input()
set_size = input()
ordered_sets = int(input())

if fruit == "Watermelon":
    if set_size == "small":
        price = 56 * 2
    elif set_size == "big":
        price = 28.7 * 5
elif fruit == "Mango":
    if set_size == "small":
        price = 36.66 * 2
    elif set_size == "big":
        price = 19.6 * 5
elif fruit == "Pineapple":
    if set_size == "small":
        price = 42.1 * 2
    elif set_size == "big":
        price = 24.8 * 5
elif fruit == "Raspberry":
    if set_size == "small":
        price = 20 * 2
    elif set_size == "big":
        price = 15.2 * 5

final_price = price * ordered_sets

if 400 <= final_price <= 1000:
    final_price = final_price * 0.85
elif final_price > 1000:
    final_price = final_price / 2

print(f"{final_price:.2f} lv.")


