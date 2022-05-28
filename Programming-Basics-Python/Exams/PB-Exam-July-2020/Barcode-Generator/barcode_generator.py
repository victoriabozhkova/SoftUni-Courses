start = (input())
end = (input())

# начин да вземем всяка една цифра в едно число:
count = 0
for i in start:
    if count == 0:
        a = int(i)
    elif count == 1:
        b = int(i)
    elif count == 2:
        c = int(i)
    elif count == 3:
        d = int(i)
    count += 1
count = 0
for j in end:
    if count == 0:
        a1 = int(j)
    elif count == 1:
        b1 = int(j)
    elif count == 2:
        c1 = int(j)
    elif count == 3:
        d1 = int(j)
    count += 1
for k in range(a, a1+1):
    for l in range(b, b1+1):
        for m in range(c, c1+1):
            for n in range(d, d1+1):
                if k % 2 != 0 and l % 2 != 0 and m % 2 != 0 and n % 2 != 0:
                    print(f"{k}{l}{m}{n}", end=" ")

