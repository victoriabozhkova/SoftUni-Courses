count_of_numbers = int(input())
left_sum = 0
right_sum = 0
for number in range(count_of_numbers * 2):
    current_number = int(input())

    if number < count_of_numbers:
        left_sum = left_sum + current_number
    else:
        right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")