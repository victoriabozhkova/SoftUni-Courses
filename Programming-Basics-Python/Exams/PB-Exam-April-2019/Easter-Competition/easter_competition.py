cakes_number = int(input())
import sys
max_points = - sys.maxsize
max_baker = ""

for i in range(1, cakes_number +1):
    baker_name = input()
    command_line = input()
    current_baker_points = 0
    while command_line != "Stop":
        points = int(command_line)
        current_baker_points += points

        if current_baker_points > max_points:
            max_points = current_baker_points
            max_baker = baker_name

        command_line = input()

    print(f"{baker_name} has {current_baker_points} points.")
    if baker_name == max_baker:
        print(f"{baker_name} is the new number 1!")

print(f"{max_baker} won competition with {max_points} points!")


