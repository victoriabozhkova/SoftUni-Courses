h = float(input())
w = float(input())

w_in_cm = w * 100
h_in_cm = h * 100

working_spaces_in_h = h_in_cm // 120
working_spaces_in_w = (w_in_cm -100 ) // 70

working_spaces = working_spaces_in_h * working_spaces_in_w -3
print(working_spaces)


