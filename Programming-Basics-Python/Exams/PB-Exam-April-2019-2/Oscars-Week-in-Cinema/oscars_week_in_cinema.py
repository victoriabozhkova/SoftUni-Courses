movie = input()
type_hall = input()
tickets = int(input())
price = 0

if movie == "A Star Is Born":
    if type_hall == "normal":
        price = 7.5
    elif type_hall == "luxury":
        price = 10.5
    elif type_hall == "ultra luxury":
        price = 13.5
elif movie == "Bohemian Rhapsody":
    if type_hall == "normal":
        price = 7.35
    elif type_hall == "luxury":
        price = 9.45
    elif type_hall == "ultra luxury":
        price = 12.75
elif movie == "Green Book":
    if type_hall == "normal":
        price = 8.15
    elif type_hall == "luxury":
        price = 10.25
    elif type_hall == "ultra luxury":
        price = 13.25
elif movie == "The Favourite":
    if type_hall == "normal":
        price = 8.75
    elif type_hall == "luxury":
        price = 11.55
    elif type_hall == "ultra luxury":
        price = 13.95

sum_price = tickets * price

print(f"{movie} -> {sum_price:.2f} lv.")
