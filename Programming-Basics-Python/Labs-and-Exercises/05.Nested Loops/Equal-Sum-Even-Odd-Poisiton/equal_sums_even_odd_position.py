start_num = int(input())
final_num = int(input())

for i in range(start_num, final_num + 1):
    number_to_str = str(i)
    odd_sum = 0
    even_sum = 0

    for j in range(0, len(number_to_str)):
        digit = int(number_to_str[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number_to_str, end = " ")


