change = float(input())

money = round(change * 100)
coins_count = 0

while money > 0:
    if money >= 200:
        money = money - 200
        coins_count += 1
    elif money >= 100:
        money = money - 100
        coins_count += 1
    elif money >= 50:
        money = money - 50
        coins_count += 1
    elif money >= 20:
        money = money - 20
        coins_count += 1
    elif money >= 10:
        money = money - 10
        coins_count += 1
    elif money >= 5:
        money = money - 5
        coins_count += 1
    elif money >= 2:
        money = money - 2
        coins_count += 1
    elif money >= 1:
        money = money - 1
        coins_count += 1

print(coins_count)




