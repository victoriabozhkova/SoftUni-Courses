number_of_rooms = int(input())

free_chairs = 0
total_chairs = 0
total_visitors = 0
the_chairs_are_enough = True
for room in range(1, number_of_rooms + 1):
    info = input().split()
    chairs = len(info[0])
    people = int(info[1])
    total_chairs += chairs
    total_visitors += people
    difference = people - chairs
    if chairs < people:
        print(f"{abs(difference)} more chairs needed in room {room}")
    elif chairs >= people:
        free_chairs += abs(difference)

if total_visitors <= total_chairs:
    print(f"Game On, {free_chairs} free chairs left")
