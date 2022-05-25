rent = int(input())
statues_price = rent * 0.7
catering_price = statues_price * 0.85
sounding_price = catering_price / 2

sum_price = rent + statues_price + catering_price + sounding_price

print(f"{sum_price:.2f}")
