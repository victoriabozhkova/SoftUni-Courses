
points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points = 5
elif points < 1000:
    bonus_points = 0.2 * points
else:
    bonus_points = 0.1 * points

if points % 2 == 0:
    bonus_points = bonus_points + 1
elif points % 5 == 0:
    bonus_points = bonus_points + 2

print(bonus_points)
print(points + bonus_points)





