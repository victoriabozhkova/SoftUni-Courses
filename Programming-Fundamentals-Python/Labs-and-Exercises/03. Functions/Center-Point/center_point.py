from math import floor


def closer_to_center(a, b, c, d):
    if abs(x1) + abs(y1) > abs(x2) + abs(y2):
        return f"({floor(x2)}, {floor(y2)})"
    elif abs(x2) + abs(y2) > abs(x1) + abs(y1):
        return f"({floor(x1)}, {floor(y1)})"
    elif abs(x1)+ abs(y1) == abs(x2)+ abs(y2):
        return f"({floor(x1)}, {floor(y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

final_point = closer_to_center(x1, y1, x2, y2)
print(final_point)
