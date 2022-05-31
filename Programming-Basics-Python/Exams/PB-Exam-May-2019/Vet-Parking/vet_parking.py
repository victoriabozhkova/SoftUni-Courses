days = int(input())
hours_for_the_day = int(input())
sum_price = 0

for day in range(1, days + 1):
    price_for_the_day = 0
    for hour in range(1, hours_for_the_day +1):
        if day % 2 == 0 and hour % 2 != 0:
            price_for_the_day += 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price_for_the_day += 1.25
        else:
            price_for_the_day += 1
    sum_price += price_for_the_day
    print(f"Day: {day} - {price_for_the_day:.2f} leva")
print(f"Total: {sum_price:.2f} leva")