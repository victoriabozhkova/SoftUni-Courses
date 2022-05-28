command_line = input()
import sys
winner_points = - sys.maxsize
winner = ""
while command_line != "Stop":
    player_name = command_line
    points_counter = 0
    for i in range(len(player_name)):
        current_number = int(input())
        current_letter = player_name[i]
        if current_number == ord(current_letter):
            points_counter += 10
        else:
            points_counter += 2
        if points_counter > winner_points:
            winner_points = points_counter
            winner = command_line
    if points_counter == winner_points:
        winner = command_line
    command_line = input()

print(f"The winner is {winner} with {winner_points} points!")
