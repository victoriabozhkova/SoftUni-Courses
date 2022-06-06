string = input()
indices_list = []
for indices, symbol in enumerate(string):
    if symbol.isupper():
        indices_list.append(indices)

print(indices_list)