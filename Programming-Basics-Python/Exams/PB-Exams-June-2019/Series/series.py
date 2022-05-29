budget = float(input())
number_of_Series = int(input())
final_price = 0

for i in range(1, number_of_Series + 1):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        series_price = series_price * 0.5
    elif series_name == "Lucifer":
        series_price = series_price * 0.6
    elif series_name == "Protector":
        series_price = series_price *0.7
    elif series_name == "TotalDrama":
        series_price = series_price * 0.8
    elif series_name == "Area":
        series_price = series_price * 0.9

    final_price += series_price

if final_price <= budget:
    print(f"You bought all the series and left with {budget - final_price:.2f} lv.")
else:
    print(f"You need {abs(final_price - budget):.2f} lv. more to buy the series!")