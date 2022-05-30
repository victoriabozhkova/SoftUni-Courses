room_rent = float(input())

cake_price = room_rent * 0.2
drinks_price = cake_price * 0.55
animator_price = room_rent / 3

final_price = room_rent +cake_price + drinks_price + animator_price

print(f"{final_price:.2f}")