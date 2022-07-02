numbers = input().split(", ")

group = 0
group_list = []
all_numbers_list = []
while True:
    group += 10

    for num in numbers:

        if group - 10 < abs(int(num)) <= group:
            group_list.append(num)
            all_numbers_list.append(num)
    current_list = [x for x in numbers if x not in group_list]
    print(f"Group of {group}'s: {[int(x) for x in group_list]}")
    group_list.clear()

    if len(all_numbers_list) == len(numbers):
        break

# my_list = [2, 3, 4, 6, 8]
# sec_list = [3, 4]
# print([i for i in my_list if i not in sec_list])

