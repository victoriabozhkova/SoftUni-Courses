moves = int(input())
points = 0
first_interval_count = 0
second_interval_count = 0
third_interval_count = 0
fourth_interval_count = 0
fifth_interval_count = 0
invalid_count = 0
for i in range(1, moves + 1):
    current_number = int(input())

    if 0 <= current_number <= 9:
        points = points + current_number * 0.2
        first_interval_count = first_interval_count +1
    elif 10 <= current_number <= 19:
        points = points + current_number * 0.3
        second_interval_count = second_interval_count + 1
    elif 20 <= current_number <= 29:
        points = points + current_number * 0.4
        third_interval_count = third_interval_count + 1
    elif 30 <= current_number <= 39:
        points = points + 50
        fourth_interval_count = fourth_interval_count + 1
    elif 40 <= current_number <= 50:
        points = points + 100
        fifth_interval_count = fifth_interval_count + 1
    elif current_number < 0 or current_number > 50:
        points = points / 2
        invalid_count = invalid_count + 1

all_numbers = first_interval_count + second_interval_count + third_interval_count + fourth_interval_count + fifth_interval_count + invalid_count

first_interval_count_percent = first_interval_count / all_numbers * 100
second_interval_count_percent = second_interval_count / all_numbers * 100
third_interval_count_percent = third_interval_count / all_numbers * 100
fourth_interval_count_percent = fourth_interval_count / all_numbers * 100
fifth_interval_count_percent = fifth_interval_count / all_numbers * 100
invalid_count_percent = invalid_count / all_numbers * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {first_interval_count_percent:.2f}%")
print(f"From 10 to 19: {second_interval_count_percent:.2f}%")
print(f"From 20 to 29: {third_interval_count_percent:.2f}%")
print(f"From 30 to 39: {fourth_interval_count_percent:.2f}%")
print(f"From 40 to 50: {fifth_interval_count_percent:.2f}%")
print(f"Invalid numbers: {invalid_count_percent:.2f}%")




