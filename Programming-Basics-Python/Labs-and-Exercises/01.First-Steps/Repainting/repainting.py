
nylon = int(input())
paint = int(input())
liquid = int(input())
hours_of_work = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = (paint + 1.1) * 14.5
price_liquid = liquid * 5
price_workers = (price_nylon + price_paint + price_liquid + 0.4) * 0.3 * hours_of_work

needed_money = price_workers + price_paint + price_liquid + price_nylon + 0.4

print(needed_money)
