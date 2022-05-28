command_line = input()


import sys
best_player_points = -sys.maxsize
best_player_name = ""

got_a_hat_trick = False

while command_line != "END":
    player_name = command_line
    number_of_goals = int(input())

    if number_of_goals > best_player_points:
        best_player_points = number_of_goals
        best_player_name = player_name

    if number_of_goals >= 3:
        got_a_hat_trick = True

    if number_of_goals >= 10:
        break

    command_line = input()

print(f"{best_player_name} is the best player!")

if got_a_hat_trick:
    print(f"He has scored {number_of_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_of_goals} goals.")