
def odd_sum(num):
    odd_digits_list = []
    for digit in num:
        if int(digit) % 2 != 0:
            odd_digits_list.append(int(digit))
    odd_digits_sum = 0
    for num in odd_digits_list:
        odd_digits_sum += num
    return odd_digits_sum


def even_sum(num):
    even_digits_list = []
    for digit in num:
        if int(digit) % 2 == 0:
            even_digits_list.append(int(digit))
    even_digits_sum = 0
    for num in even_digits_list:
        even_digits_sum += num
    return even_digits_sum


number = input()

odd_digits_sum = odd_sum(number)
even_digits_sum = even_sum(number)

print(f"Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}")












