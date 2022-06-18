product = input()
quantity = int(input())


def final_price(a, b):
    if product == "coffee":
        price = 1.5
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00
    result = price * quantity
    return f"{result:.2f}"


print(final_price(product, quantity))


