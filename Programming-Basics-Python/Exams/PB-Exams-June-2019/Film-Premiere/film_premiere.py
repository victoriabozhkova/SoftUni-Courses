movie = input()
movie_pack = input()
tickets = int(input())
ticket_price = 0

if movie == "John Wick":
    if movie_pack == "Drink":
        ticket_price = 12
    elif movie_pack == "Popcorn":
        ticket_price = 15
    elif movie_pack == "Menu":
        ticket_price = 19
elif movie == "Star Wars":
    if movie_pack == "Drink":
        ticket_price = 18
    elif movie_pack == "Popcorn":
        ticket_price = 25
    elif movie_pack == "Menu":
        ticket_price = 30
    if tickets >= 4:
        ticket_price = ticket_price * 0.70
elif movie == "Jumanji":
    if movie_pack == "Drink":
        ticket_price = 9
    elif movie_pack == "Popcorn":
        ticket_price = 11
    elif movie_pack == "Menu":
        ticket_price = 14
    if tickets == 2:
        ticket_price = ticket_price * 0.85

final_price = ticket_price * tickets

print(f"Your bill is {final_price:.2f} leva.")

