x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

first_condition = True
second_condition = True

if (x == x1 or x == x2) and (y >= y1 and y <= y2):
    first_condition = True
elif (y == y1 or y == y2) and (x >= x1 and x <= x2):
    second_condition = True
else:
    first_condition = False
    second_condition = False


if first_condition == True or second_condition == True:
    print("Border")
else:
    print("Inside / Outside")






