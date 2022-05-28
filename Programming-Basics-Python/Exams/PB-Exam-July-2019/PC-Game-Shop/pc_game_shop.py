sold_games = int(input())
games_in_hearthstone = 0
games_in_fornite = 0
games_in_overwatch = 0
games_in_others = 0
for i in range(1, sold_games + 1):
    game = input()
    if game == "Hearthstone":
        games_in_hearthstone += 1
    elif game == "Fornite":
        games_in_fornite += 1
    elif game == "Overwatch":
        games_in_overwatch += 1
    else:
        games_in_others += 1


percent_hearthstone = games_in_hearthstone / sold_games * 100
percent_overwatch = games_in_overwatch / sold_games * 100
percent_fornite = games_in_fornite / sold_games * 100
percent_others = games_in_others / sold_games * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")

