student_name = input()
current_class = 1
grades_count = 0
bad_tries = 0
is_expelled = False
while current_class <= 12:
    final_grade = float(input())

    if final_grade < 4:
        bad_tries += 1
        if bad_tries == 2:
            is_expelled = True
            break
        continue

    current_class += 1
    grades_count += final_grade

average_grade = grades_count / 12

if is_expelled:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
