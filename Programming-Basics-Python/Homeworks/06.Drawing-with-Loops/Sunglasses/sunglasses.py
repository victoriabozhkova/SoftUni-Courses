n = int(input())

spaces = "/"
stars = "*"
interval = " "
middle = n // 2

print(f"{stars}" * (n * 2) + f"{interval}" * (n) + f"{stars}" * (n *2))

for base in range(1, n-1):
    if (n % 2 == 0 and base + 1 == middle):
        interval = "|"
    elif (n % 2 != 0 and base == middle):
        interval = "|"
    else:
        interval = " "
    print(f"{stars}" + f"{spaces}" * (n * 2- 2) + f"{stars}" + f"{interval}" * n + f"{stars}" + f"{spaces}" * (n * 2-2)
          + f"{stars}")

interval = " "

print(f"{stars}" * (n * 2) + f"{interval}" * (n) + f"{stars}" * (n *2))

