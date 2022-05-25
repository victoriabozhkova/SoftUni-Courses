n = int(input())
stars = "*"
minus = "-"
pipes = "|"



for i in range(1, (n+1)//2+1):
    if n % 2 == 0:
        if i == 1:
            print(f"{minus}" * ((n + 1) // 2 - 1) + f"{stars}" * 2 + f"{minus}" * ((n + 1) // 2 - 1))
        else:
            print(f"{minus}" * ((n + 1) // 2 -i) + f"{stars}" * (i*2) + f"{minus}" * ((n + 1) // 2-i))
    else:
        if i == 1:
            print(f"{minus}" * ((n + 1) // 2 - 1) + f"{stars}" + f"{minus}" * ((n + 1) // 2 - 1))
        else:
            print(f"{minus}" * ((n + 1) // 2 - i) + f"{stars}" * (i*2-1) + f"{minus}" * ((n + 1) // 2 -i))

for i in range(1, n//2+1):
    print(f"{pipes}" + f"{stars}" * (n-2) + f"{pipes}")




