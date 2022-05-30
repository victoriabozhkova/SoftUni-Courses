capacity = float(input())
command_line = input()
luggage_counter = 0
left_capacity = capacity
is_space_not_left = False

while command_line != "End":
    luggage_size = float(command_line)

    if (luggage_counter + 1) % 3 == 0:
        luggage_size = luggage_size * 1.1

    if luggage_size > left_capacity:
        is_space_not_left = True
        break

    left_capacity -= luggage_size

    luggage_counter += 1

    if left_capacity <= 0:
        break



    command_line = input()

if is_space_not_left:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {luggage_counter} suitcases loaded.")