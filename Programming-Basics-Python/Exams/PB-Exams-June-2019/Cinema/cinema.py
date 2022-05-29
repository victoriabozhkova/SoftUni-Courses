capacity = int(input())
sum_taken_seats = 0
price_ticket = 5
profit = 0
is_hall_full = False

command_line = input()
while command_line != "Movie time!":
    taken_seats = int(command_line)
    if taken_seats > capacity - sum_taken_seats:
        is_hall_full = True
        break
    sum_taken_seats += taken_seats
    current_price = 0

    if taken_seats % 3 == 0:
        current_price = taken_seats * price_ticket - 5
    else:
        current_price = taken_seats * price_ticket

    profit += current_price
    command_line = input()

if is_hall_full:
    print(f"The cinema is full.")
elif command_line == "Movie time!":
    print(f"There are {capacity - sum_taken_seats} seats left in the cinema.")
print(f"Cinema income - {profit} lv.")



