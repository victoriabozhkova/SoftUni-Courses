filming_time = int(input())
scenes = int(input())
scene_time = int(input())

set_prep = filming_time * 0.15
scene_filming = scenes * scene_time
time_sum = set_prep + scene_filming

if time_sum <= filming_time:
    print(f"You managed to finish the movie on time! You have {round(filming_time- time_sum)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_sum - filming_time)} minutes.")