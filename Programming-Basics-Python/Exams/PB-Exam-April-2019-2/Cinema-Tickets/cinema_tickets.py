input_line = input()
standard_counter = 0
student_counter = 0
kid_counter =0
sum_tickets = 0
while input_line != "Finish":
    movie_name = input_line
    free_seats = int(input())
    current_movie_counter = 0
    command_line = input()
    while command_line != "End":
        type_ticket = command_line
        sum_tickets += 1
        current_movie_counter += 1
        if type_ticket == "standard":
            standard_counter += 1
        elif type_ticket == "student":
            student_counter += 1
        elif type_ticket == "kid":
            kid_counter += 1
        if current_movie_counter == free_seats:
            break


        command_line = input()
    percent_full = current_movie_counter / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    input_line = input()

print(f"Total tickets: {sum_tickets}")
avg_student_tickets = student_counter / sum_tickets * 100
print(f"{avg_student_tickets:.2f}% student tickets.")
avg_standard_tickets = standard_counter / sum_tickets * 100
print(f"{avg_standard_tickets:.2f}% standard tickets.")
avg_kid_tickets = kid_counter / sum_tickets * 100
print(f"{avg_kid_tickets:.2f}% kids tickets.")



