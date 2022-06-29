employees_happiness = list(map(int, input().split()))
factor = int(input())

multiplied_happiness = list(map(lambda x: x * factor, employees_happiness))

total_happiness = sum(multiplied_happiness)
avg_happiness = total_happiness / len(multiplied_happiness)

filtered = list(filter(lambda x: x >= avg_happiness, multiplied_happiness))

if len(filtered) >= len(multiplied_happiness) // 2:
    print(f"Score: {len(filtered)}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(multiplied_happiness)}. Employees are not happy!")