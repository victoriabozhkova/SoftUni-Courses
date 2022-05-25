students_at_exam = int(input())
between_2_and_2_99 = 0
between_3_and_3_99 = 0
between_4_and_4_99 = 0
between_5_and_6 = 0
exam_grade_sum = 0
for i in range(1, students_at_exam + 1):
    exam_grade = float(input())

    if 2 <= exam_grade <= 2.99:
        between_2_and_2_99 = between_2_and_2_99 + 1
    elif 3 <= exam_grade <= 3.99:
        between_3_and_3_99 = between_3_and_3_99 +1
    elif 4<= exam_grade <= 4.99:
        between_4_and_4_99 = between_4_and_4_99 + 1
    elif 5 <= exam_grade <= 6:
        between_5_and_6 = between_5_and_6 + 1

    exam_grade_sum = exam_grade_sum + exam_grade

between_2_and_2_99_percent = between_2_and_2_99 / students_at_exam * 100
between_3_and_3_99_percent = between_3_and_3_99 / students_at_exam * 100
between_4_and_4_99_percent = between_4_and_4_99 / students_at_exam * 100
between_5_and_6_percent = between_5_and_6 / students_at_exam * 100

average_grade = exam_grade_sum / students_at_exam
print(f"Top students: {between_5_and_6_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99_percent:.2f}%")
print(f"Fail: {between_2_and_2_99_percent:.2f}%")
print(f"Average: {average_grade:.2f}")



