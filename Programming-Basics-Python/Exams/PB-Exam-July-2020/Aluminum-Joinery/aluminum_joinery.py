number_of_joinery = int(input())
type = input()
delivery = input()
price = 0

if type == "90X130":
    price = 110
    if number_of_joinery > 60:
        price = price * 0.92
    elif number_of_joinery > 30:
        price = price * 0.95
elif type == "100X150":
    price = 140
    if number_of_joinery > 80:
        price = price * 0.9
    elif number_of_joinery > 40:
        price = price * 0.94
elif type == "130X180":
    price = 190
    if number_of_joinery > 50:
        price = price * 0.88
    elif number_of_joinery > 20:
        price = price * 0.93
elif type == "200X300":
    price = 250
    if number_of_joinery > 50:
        price = price * 0.86
    elif number_of_joinery > 25:
        price = price * 0.91

final_price = number_of_joinery * price

if delivery == "With delivery":
    final_price += 60
else:
    pass

if number_of_joinery > 99:
    final_price = final_price * 0.96

if number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{final_price:.2f} BGN")





