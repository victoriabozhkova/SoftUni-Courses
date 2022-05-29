series_name = input()
seasons = int(input())
episodes = int(input())
episode_time = float(input())

episode_time_w_ads = episode_time * 1.2
last_episode = episode_time_w_ads + 10
sum_episodes_time = (episodes - 1) * episode_time_w_ads + last_episode
seasons_time = seasons * sum_episodes_time
import math
print(f"Total time needed to watch the {series_name} series is {math.floor(seasons_time)} minutes.")