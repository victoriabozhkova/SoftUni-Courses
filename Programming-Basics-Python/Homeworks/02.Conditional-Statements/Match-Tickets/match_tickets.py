budget = float(input())
category = input()
people_in_a_group = int(input())
ticket_price = 0
transport_budget = 0

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

if 1 <= people_in_a_group <=4:
    transport_budget = budget * 0.75
elif 5 <= people_in_a_group <= 9:
    transport_budget = budget * 0.6
elif 10 <= people_in_a_group <= 24:
    transport_budget = budget * 0.5
elif 25 <= people_in_a_group <= 49:
    transport_budget = budget * 0.4
elif 50 <= people_in_a_group:
    transport_budget = budget * 0.25

money_left = budget - transport_budget

if money_left >= ticket_price*people_in_a_group:
    print(f"Yes! You have {(money_left-ticket_price*people_in_a_group):.2f} leva left.")
elif money_left < ticket_price*people_in_a_group:
    print(f"Not enough money! You need {(ticket_price*people_in_a_group-money_left):.2f} leva.")


