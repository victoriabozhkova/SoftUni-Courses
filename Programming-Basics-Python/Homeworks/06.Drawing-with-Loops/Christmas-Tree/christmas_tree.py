n = int(input())
interval = " "
stars = "*"
pipe = "|"

for i in range(0, n+1):
    print(f"{interval}" * (n-i) + f"{stars}" * i + f" {pipe} " + f"{stars}" * i + f"{interval}" * (n - i))