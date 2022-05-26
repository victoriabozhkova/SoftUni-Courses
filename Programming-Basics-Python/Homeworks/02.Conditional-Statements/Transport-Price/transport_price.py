km = int(input())
time_of_day = input()
taxi_init_price = 0.7
taxi_day_price = 0.79
taxi_night_price = 0.9
bus_price = 0.09
train_price = 0.06

if time_of_day == "day":
    price_sum = taxi_init_price + taxi_day_price * km
    if km >= 100:
        price_sum = train_price * km
    elif km >= 20:
        price_sum = bus_price * km

elif time_of_day == "night":
    price_sum = taxi_init_price + taxi_night_price * km
    if km >= 100:
        price_sum = train_price * km
    elif km >= 20:
        price_sum = bus_price * km

print(f"{price_sum:.2f}")
