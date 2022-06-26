def multiplication_negative(x, y, z):
    list_of_numbers = [x, y, z]
    negative_count = 0
    for number in list_of_numbers:
        if number < 0:
            negative_count += 1
    if negative_count % 2 != 0:
        return True

def miltiplication_zero(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return True


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


if multiplication_negative(number_1, number_2, number_3):
    if miltiplication_zero(number_1, number_2, number_3):
        print("zero")
    else:
        print("negative")
elif not multiplication_negative(number_1, number_2, number_3):
    if miltiplication_zero(number_1, number_2, number_3):
        print("zero")
    else:
        print("positive")




