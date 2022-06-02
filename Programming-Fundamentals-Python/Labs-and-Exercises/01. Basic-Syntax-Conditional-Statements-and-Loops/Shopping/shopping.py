budget = int(input())
command = input()
budget_left = budget
while command != "End":
    price = int(command)
    if price > budget_left:
        print("You went in overdraft!")
        break

    budget_left -= price
    command = input()

else:
    print("You bought everything needed.")

