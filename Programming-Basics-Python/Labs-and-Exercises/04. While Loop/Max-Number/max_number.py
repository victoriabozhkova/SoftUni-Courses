import sys

command = input()
max_number = -sys.maxsize

while command != "Stop":
    current_number = int(command)
    command = input()

    if current_number > max_number:
        max_number = current_number

    if command == "Stop":
        break

print(max_number)
