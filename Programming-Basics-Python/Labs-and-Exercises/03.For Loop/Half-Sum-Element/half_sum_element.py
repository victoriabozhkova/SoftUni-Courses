
import sys
numbers = int(input())
max_number = -sys.maxsize
sum = 0

for i in range(1, numbers + 1):
    number = int(input())
    sum = sum + number

    if number > max_number:
        max_number = number

sum = sum - max_number


if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(sum-max_number)}")


