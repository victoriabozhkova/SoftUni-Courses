
tv_show = input()
episode_time = int(input())
lunch_break = int(input())

lunch_time = lunch_break * 1/8
break_time = lunch_break * 1/4
import math
time_left = lunch_break - lunch_time - break_time
if time_left >= episode_time:
    print(f"You have enough time to watch {tv_show} and left with {math.ceil(time_left - episode_time)} minutes free time.")
elif time_left < episode_time:
    print(f"You don't have enough time to watch {tv_show}, you need {math.ceil(episode_time - time_left)} more minutes.")

