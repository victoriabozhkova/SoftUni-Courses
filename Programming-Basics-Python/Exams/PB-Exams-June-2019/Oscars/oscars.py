actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

points = 0

for i in range(1, number_of_judges + 1):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2
    sum_points = points + academy_points

    if sum_points > 1250.5:
        break

if sum_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {sum_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - sum_points:.1f} more!")