team_name = input()
played_games = int(input())
win_points_counter = 0
naravno_points_counter = 0
lost_games_counter = 0
wins_counter = 0
naravno_counter = 0
total_points = 0

for i in range(1, played_games + 1):
    result = input()
    if result == "W":
        win_points_counter += 3
        wins_counter += 1
    elif result == "D":
        naravno_points_counter += 1
        naravno_counter += 1
    else:
        lost_games_counter += 1

if played_games > 0:
    percent_wins = wins_counter / played_games * 100
total_points = win_points_counter + naravno_points_counter

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_counter}")
    print(f"## D: {naravno_counter}")
    print(f"## L: {lost_games_counter}")
    print(f"Win rate: {percent_wins:.2f}%")



