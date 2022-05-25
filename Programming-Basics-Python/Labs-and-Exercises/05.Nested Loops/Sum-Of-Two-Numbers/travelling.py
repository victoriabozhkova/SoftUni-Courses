destination = input()

while destination != "End":
    money_needed = float(input())
    collected_money = 0
    while money_needed > collected_money:
        saved_money = float(input())
        collected_money += saved_money
    print(f"Going to {destination}!")
    destination = input()





