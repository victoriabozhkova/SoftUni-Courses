men = int(input())
women = int(input())
tables = int(input())
couples_counter = 0
couples = ""

while couples_counter <= tables:
    if couples_counter == men * women:
        break
    elif couples_counter == tables:
        break
    for i in range(1, men+1):
        if couples_counter == tables:
            break
        for j in range(1, women+1):
            if couples_counter == tables:
                break
            couples_counter += 1
            couples = f"({i} <-> {j})"
            print(couples, end=" ")

