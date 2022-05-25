interval_start = int(input())
interval_final = int(input())
magic_number = int(input())
counter = 0
is_combination_found = False

for first_number in range(interval_start, interval_final +1):
    for second_number in range(interval_start, interval_final +1):
        counter += 1
        if first_number + second_number == magic_number:
            is_combination_found = True
            break
    if is_combination_found:
        break

if is_combination_found:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
