def loading_bar(percent):
    if percent == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        symbol = "%"
        dots = "."
        number_of_symbols = percent // 10
        number_of_dots = 10 - number_of_symbols
        print(f"{percent}" + "% " + "[" +  f"{symbol}" * number_of_symbols + f"{dots}" * number_of_dots + "]")
        print("Still loading...")


number = int(input())
loading_bar(number)