number_of_guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    price_per_person = price_per_person * 0.85
elif 15 < number_of_guests <= 20:
    price_per_person = price_per_person * 0.8
elif number_of_guests > 20:
    price_per_person = price_per_person * 0.75
else:
    pass

price_all_guests = number_of_guests * price_per_person
sum_price = price_all_guests + budget * 0.1

if sum_price > budget:
    print(f"No party! {sum_price-budget:.2f} leva needed.")
else:
    print(f"It is party time! {abs(sum_price-budget):.2f} leva left.")
