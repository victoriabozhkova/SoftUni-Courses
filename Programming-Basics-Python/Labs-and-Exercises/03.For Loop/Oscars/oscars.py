actor_name = input()
initial_points = float(input())
count_judges = int(input())
sum_points = initial_points
for i in range(1, count_judges + 1):
    judge_name = input()
    judge_points = float(input())
    length = len(judge_name)
    points = judge_points * length / 2
    sum_points = sum_points + points

    if sum_points >= 1250.5:
        break

if sum_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {sum_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5-sum_points:.1f} more!")


