wanted_profit = int(input())
command = input()
transaction_num = 0
collected_money = 0
cash_payment_counter = 0
card_payment_counter = 0
card_sum = 0
cash_sum = 0
while command != "End":
    product_price = int(command)
    transaction_num += 1

    if transaction_num % 2 == 1:
        if product_price > 100:
            print("Error in transaction!")
        else:
            collected_money += product_price
            cash_sum += product_price
            cash_payment_counter += 1
            print("Product sold!")
    elif transaction_num % 2 == 0:
        if product_price < 10:
            print("Error in transaction!")
        else:
            collected_money += product_price
            card_payment_counter += 1
            card_sum += product_price
            print("Product sold!")

    if collected_money >= wanted_profit:
        break

    if command == "End":
        break

    command = input()

if card_payment_counter > 0:
    average_card_payment = card_sum / card_payment_counter
if cash_payment_counter > 0:
    average_cash_payment = cash_sum / cash_payment_counter

if collected_money >= wanted_profit:
    print(f"Average CS: {average_cash_payment:.2f}")
    print(f"Average CC: {average_card_payment:.2f}")
else:
    print("Failed to collect required money for charity.")


