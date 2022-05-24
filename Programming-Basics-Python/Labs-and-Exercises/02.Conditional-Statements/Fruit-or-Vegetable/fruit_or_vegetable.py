product = input()
product_is_fruit = 0
product_is_vegie = 0

if product == "banana"\
    or product == "apple"\
    or product == "kiwi"\
    or product == "cherry"\
    or product == "lemon"\
    or product == "grapes":
    product_is_fruit = True
elif product == "tomato"\
    or product == "cucumber"\
    or product == "pepper"\
    or product == "carrot":
    product_is_vegie = True
else:
    pass

if product_is_fruit == True:
    print("fruit")
elif product_is_vegie == True:
    print("vegetable")
else:
    print("unknown")