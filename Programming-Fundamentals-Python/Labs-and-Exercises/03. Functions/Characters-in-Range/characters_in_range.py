def symbols(a, b):
    symbols_list = []
    for symbols in range(ord(a) + 1, ord(b)):
        symbols_list.append(chr(symbols))

    return " ".join(symbols_list)


character_one = input()
character_two = input()

print(symbols(character_one, character_two))



