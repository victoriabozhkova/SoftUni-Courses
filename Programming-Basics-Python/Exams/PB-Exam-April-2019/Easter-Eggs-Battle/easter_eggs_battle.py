first_player_eggs = int(input())
second_player_eggs = int(input())
is_game_over = False
command_line = input()
while command_line != "End":
    if command_line == "one":
        second_player_eggs -= 1
    elif command_line == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0 or second_player_eggs == 0:
        is_game_over = True
        break

    command_line = input()

if is_game_over:
    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
    elif second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
