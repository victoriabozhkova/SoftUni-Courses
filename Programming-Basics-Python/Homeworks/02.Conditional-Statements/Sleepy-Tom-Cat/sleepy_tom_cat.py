free_days = int(input())

game_time = 30000
work_days_game_time_per_day = 63
free_days_game_time_per_day = 127

days_in_a_year = 365
work_days_in_a_year = days_in_a_year - free_days

work_days_game_time_sum = work_days_game_time_per_day * work_days_in_a_year
free_days_game_time_sum = free_days_game_time_per_day * free_days

import math
game_time_sum = work_days_game_time_sum + free_days_game_time_sum
diff_time = game_time_sum - game_time
hours_game_time = diff_time / 60
min_game_time = diff_time % 60

if game_time_sum > game_time:
    print(f"Tom will run away")
    print(f"{math.floor(abs(hours_game_time))} hours and {math.floor(abs(min_game_time))} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{math.floor(abs(hours_game_time))} hours and {60 - min_game_time} minutes less for play")
