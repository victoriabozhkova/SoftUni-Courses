import sys

command = input()
min_number = sys.maxsize

while command != "Stop":
    current_number = int(command)
    command = input()

    if current_number < min_number:
        min_number = current_number

    if command == "Stop":
        break

print(min_number)
