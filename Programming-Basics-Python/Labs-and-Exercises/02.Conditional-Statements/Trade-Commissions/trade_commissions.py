city = input()
sales = float(input())
commission = 0
city_is_valid = True
sales_are_valid = True

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
    else:
        sales_are_valid = False
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
    else:
        sales_are_valid = False
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.1
    elif city == "Plovdiv":
        commission = 0.12
    else:
        sales_are_valid = False
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
    else:
        sales_are_valid = False
else:
    city_is_valid = False

final_money = sales * commission

if city_is_valid == True and sales_are_valid == True:
    print(f"{final_money:.2f}")
else:
    print("error")


