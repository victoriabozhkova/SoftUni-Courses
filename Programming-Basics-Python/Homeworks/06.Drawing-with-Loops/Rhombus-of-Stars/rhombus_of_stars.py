n = int(input())
interval = " "
star = "*"

for row in range(1, n):
    print(f"{interval}" * (n-row) + f"{star} " + f"{star} " * (row-1))

print(f"{star} " * n)

for row in range(n-1, 1-1, -1):
    print(f"{interval}" * (n - row) + f"{star} " + f"{star} " * (row - 1))