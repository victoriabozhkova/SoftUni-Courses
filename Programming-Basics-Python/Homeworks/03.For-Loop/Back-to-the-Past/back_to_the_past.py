legacy_money = float(input())
year_to_live = int(input())
age = 17
money_left = legacy_money
for current_year in range(1800, year_to_live+1):
    age = age + 1

    if current_year % 2 == 0:
        money_left = money_left - 12000
    else:
        money_left = money_left - (12000 + age * 50)

if money_left < 0:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
elif 0 <= money_left <= legacy_money:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")