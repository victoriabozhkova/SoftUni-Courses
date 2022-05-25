n = int(input())
plus = "+"
minus = "-"
pipes = "|"

print(f"{plus} " + f"{minus} " * (n- 2) + f"{plus} ")
for i in range(1, n-1):
    print(f"{pipes} " + f"{minus} " * (n-2) + f"{pipes} ")

print(f"{plus} " + f"{minus} " * (n- 2) + f"{plus} ")
