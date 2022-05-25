days = int(input())
hours_per_day = int(input())
price_even_day = 2.5
price_odd_day = 1.25
price_else = 1
sum_price_even = 0
sum_price_odd = 0
sum_price_else = 0
sum_price = 0
sum_price_days = 0
for i in range(1, days +1):
    for j in range(1, hours_per_day +1):
        if i % 2 == 0 and j % 2 == 1:
            sum_price_even += price_even_day
        elif i % 2 ==1 and j % 2 == 0:
            sum_price_odd += price_odd_day
        else:
            sum_price_else += price_else
        sum_price = sum_price_even + sum_price_odd + sum_price_else
    print(f"Day: {i} - {sum_price:.2f} leva", end="")
    print()
    sum_price_days += sum_price
    sum_price_even = 0
    sum_price_odd = 0
    sum_price_else = 0
    sum_price = 0

print(f"Total: {sum_price_days:.2f} leva")
days = int(input())
hours_per_day = int(input())
price_even_day = 2.5
price_odd_day = 1.25
price_else = 1
sum_price_even = 0
sum_price_odd = 0
sum_price_else = 0
sum_price = 0
sum_price_days = 0
for i in range(1, days +1):
    for j in range(1, hours_per_day +1):
        if i % 2 == 0 and j % 2 == 1:
            sum_price_even += price_even_day
        elif i % 2 ==1 and j % 2 == 0:
            sum_price_odd += price_odd_day
        else:
            sum_price_else += price_else
        sum_price = sum_price_even + sum_price_odd + sum_price_else
    print(f"Day: {i} - {sum_price:.2f} leva", end="")
    print()
    sum_price_days += sum_price
    sum_price_even = 0
    sum_price_odd = 0
    sum_price_else = 0
    sum_price = 0

print(f"Total: {sum_price_days:.2f} leva")
