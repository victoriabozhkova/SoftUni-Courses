last_sector = input()
rows_in_first_sector= int(input())
seats_odd_row = int(input())
first_sector = ord("A")
first_seat = ord("a")
counter_seats = 0

for sector in range(first_sector, ord(last_sector) + 1):
    for row in range(1, rows_in_first_sector + 1):
        if row % 2 != 0:
            for seats in range(first_seat, (first_seat + seats_odd_row)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                counter_seats += 1
        elif row % 2 == 0:
            for seats in range(first_seat, (first_seat + seats_odd_row + 2)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                counter_seats += 1
    if rows_in_first_sector + 1 > rows_in_first_sector:
        rows_in_first_sector += 1

print(counter_seats)


