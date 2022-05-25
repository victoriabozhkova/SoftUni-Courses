n = int(input())

star = "*"
minus = "-"
rows = 0
middle = n // 2

if n % 2 == 0:
    rows = n -1
else:
    rows = n

for i in range(1, rows + 1):
    if n % 2 == 0:
        if i == 1:
            print(f"{minus}" * ((n-1)//2) + f"{star}" * 2 + f"{minus}" * ((n-1)//2))
        elif middle - i <0:
           break
        else:
            print(f"{minus}" * ((n-1)//2 - i + 1 ) + f"{star}" + f"{minus}" * (i * 2 - 2) + f"{star}" + f"{minus}" * ((n-1)//2-i+1))
    elif n % 2 == 1:
        if i ==1:
            print(f"{minus}" * ((n-1)//2) + f"{star}" + f"{minus}" * ((n-1)//2))
        elif middle - i +1 <0:
            break
        else:
            print(f"{minus}" * ((n-1)//2 - i +1) + f"{star}" + f"{minus}" * (i*2-3) + f"{star}" + f"{minus}" * ((n-1)//2-i+1))

for j in range((n-1)//2, 1-1, -1):
    if n % 2 == 0:
        if j == 0:
            print(f"{minus}" * ((n - 1) // 2) + f"{star}" * 2 + f"{minus}" * ((n - 1) // 2))
        else:
            print(f"{minus}" * ((n-1)//2 - j +1) + f"{star}" + f"{minus}" * (j * 2 -2) + f"{star}" + f"{minus}" * ((n-1)//2 - j +1))
    elif n % 2 == 1:
        if j == 1:
            print(f"{minus}" * ((n - 1) // 2) + f"{star}" + f"{minus}" * ((n - 1) // 2))
        else:
            print(f"{minus}" * ((n-1)//2 - j +1) + f"{star}" + f"{minus}" * (j * 2 -3) + f"{star}" + f"{minus}" * ((n-1)//2 - j +1))
