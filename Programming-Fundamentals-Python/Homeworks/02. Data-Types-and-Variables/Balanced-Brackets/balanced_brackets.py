number_of_lines = int(input())
balance_symbols = ''
is_balanced_combination = False
balanced_combination = ["()", ")("]
for i in range(number_of_lines):
    symbol = input()
    if balance_symbols == "(" and symbol != ")":
        is_balanced_combination = False
    elif balance_symbols == ")" and symbol != "(":
        is_balanced_combination = False
    if symbol == "(":
        balance_symbols += symbol
    elif symbol == ")":
        balance_symbols += symbol
    if balance_symbols in balanced_combination:
        is_balanced_combination = True

if is_balanced_combination:
    print("BALANCED")
elif is_balanced_combination == False:
    print("UNBALANCED")



