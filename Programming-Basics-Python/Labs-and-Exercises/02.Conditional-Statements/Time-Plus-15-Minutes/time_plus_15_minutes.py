#По най-сложния начин:
hour = int(input())
minute = int(input())
hours = 0
minutes = 0

if 0 <= hour <= 23 and 0 <= minute <= 44:
    hours = hour
    minutes = minute + 15
    print(f"{hours}:{minutes}")
elif 0 <= hour <= 22 and 45 <= minute <= 54:
    hours = hour + 1
    minutes = minute % 15
    print(f"{hours}:0{minutes}")
elif 0 <= hour <=22 and 59 >= minute >= 55:
    hours = hour + 1
    minutes = minute % 15
    print(f"{hours}:{minutes}")
elif hour == 23 and 45 <= minute <= 54:
    hours = "0"
    minutes = minute % 15
    print(f"{hours}:0{minutes}")
elif hour == 23 and 59 >= minute >= 55:
    hours == "0"
    minutes = minute % 15
    print(f"{hours}:{minutes}")

#hours = int(input())
#minutes = int(input())

#minutes += 15

#if minutes >= 60:
#    hours +=1
#    minutes = minutes % 60

#if hours > 23:
#    hours = 0

#if minutes <= 9:
#    print(f'{hours}:0{minutes}')
#else: print(f'{hours}:{minutes}')










