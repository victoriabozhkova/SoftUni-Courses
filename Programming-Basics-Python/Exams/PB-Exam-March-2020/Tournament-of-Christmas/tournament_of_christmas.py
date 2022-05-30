
tour_days = int(input())
days_count = 0

total_wins = 0
total_loses = 0
final_money = 0
is_winner = False
tour_end = False
while not tour_end:
    daily_wins = 0
    daily_money = 0
    daily_loses = 0
    while days_count <= tour_days:
        command = input()

        if command == "Finish":
            break

        result = input()
        if result == "win":
            daily_wins += 1
            total_wins += 1
            daily_money += 20
        elif result == "lose":
            daily_loses += 1
            total_loses += 1

    if daily_wins > daily_loses:
        daily_money *= 1.1
    elif daily_wins < daily_loses:
        tour_end = False
    final_money += daily_money
    days_count += 1
    if days_count < tour_days:
        tour_end = False
        continue
    else:
        tour_end = True
        break
if total_wins > total_loses:
    final_money *= 1.2
    print(f"You won the tournament! Total raised money: {final_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {final_money:.2f}")