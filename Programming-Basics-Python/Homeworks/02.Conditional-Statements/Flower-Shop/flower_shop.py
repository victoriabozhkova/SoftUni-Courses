magnolias = int(input())
zyumbyuli = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

magnolia_price = 3.25
zyumbyul_price = 4
rose_price = 3.5
cactus_price = 8

order_price = magnolia_price * magnolias + zyumbyul_price * zyumbyuli + rose_price * roses + cactus_price * cactuses
final_money = order_price * 0.95

import math
if final_money >= gift_price:
    print(f"She is left with {math.floor(final_money-gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price-final_money)} leva." )