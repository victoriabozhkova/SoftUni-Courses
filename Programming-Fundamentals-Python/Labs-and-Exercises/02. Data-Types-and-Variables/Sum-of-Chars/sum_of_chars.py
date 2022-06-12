number_of_symbols = int(input())
total_sum = 0

for i in range(number_of_symbols):
    string = input()
    total_sum += ord(string)

print(f"The sum equals: {total_sum}")
