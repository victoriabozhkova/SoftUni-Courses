number_of_lines = int(input())
capacity = 255

while not capacity <= 0:
    for i in range(number_of_lines):
        liters_of_water = int(input())
        if capacity < liters_of_water:
            print("Insufficient capacity!")
            continue
        capacity -= liters_of_water

    left_capacity = 255 - capacity
    print(left_capacity)
    break
