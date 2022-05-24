exam_hour = int(input())
exam_minutes = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = hour_of_arrival * 60 + minutes_of_arrival

diff_minutes = abs(exam_time - arrival_time)

if exam_time < arrival_time:
    print("Late")
    if diff_minutes <= 59:
        print(f"{diff_minutes} minutes after the start")
    elif (arrival_time-exam_time)%60 <=9:
        print(f"{hour_of_arrival-exam_hour}:0{diff_minutes%60} hours after the start")
    elif arrival_time - exam_time > 59:
        print(f"{hour_of_arrival-exam_hour}:{diff_minutes%60} hours after the start")
elif 1 <= exam_time - arrival_time <= 30 and exam_time != arrival_time:
    print("On time")
    if exam_time != arrival_time:
        print(f"{diff_minutes} minutes before the start")
elif exam_time - arrival_time > 30:
    print("Early")
    if exam_time - arrival_time <= 59:
        print(f"{diff_minutes} minutes before the start")
    elif (exam_time-arrival_time)%60 <= 9:
        print(f"{exam_hour-hour_of_arrival}:0{diff_minutes%60} hours before the start")
    elif exam_time - arrival_time >= 60:
        print(f"{exam_hour-hour_of_arrival}:{diff_minutes%60} hours before the start")

# exam_time_in_minutes = exam_hour * 60 + exam_minutes
# arrival_time_in_minutes = hour_of_arrival * 60 + minutes_of_arrival
#
# diff_minutes = abs(exam_time_in_minutes - arrival_time_in_minutes)
#
# if exam_time_in_minutes < arrival_time_in_minutes:
#     print("Late")
#     if diff_minutes >= 60:
#         hour = diff_minutes // 60
#         minutes = diff_minutes % 60
#         if minutes < 10:
#             print(f"{hour}:0{minutes} hours after the start")
#         else:
#             print(f"{hour}:{minutes} hours after the start")
#     else:
#         print(f"{diff_minutes} minutes after the start")
# elif exam_time_in_minutes == arrival_time_in_minutes or diff_minutes <= 30:
#     print("On time")
#     if diff_minutes >=1 and diff_minutes <= 30:
#         print(f"{diff_minutes} minutes before the start")
# else:
#     print("Early")
#     if diff_minutes >= 60:
#         hour = diff_minutes // 60
#         minutes = diff_minutes % 60
#         if minutes <= 9:
#             print(f"{hour}:0{minutes} hours before the start")
#         else:
#             print(f"{hour}:{minutes} hours before the start")
#     else:
#         print(f"{diff_minutes} minutes before the start")
