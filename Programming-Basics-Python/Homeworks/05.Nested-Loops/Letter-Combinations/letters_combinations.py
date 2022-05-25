interval_start = input()
interval_finish = input()
missed_letter = input()
combination_is_valid = False
valid_counter = 0

for i in range(ord(interval_start), ord(interval_finish) + 1):
    for j in range(ord(interval_start), ord(interval_finish) + 1):
        for k in range(ord(interval_start), ord(interval_finish) + 1):
            if i != ord(missed_letter) and j != ord(missed_letter) and k != ord(missed_letter):
                combination_is_valid = True
                valid_counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end = " ")
print(valid_counter)

