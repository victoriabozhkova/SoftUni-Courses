from math import floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # to find the closest coordinate we must square each of the points rather than finding their sum, e.g. (1, 1) and
    # (2, 0) have equal sum values but (1, 1) is closer to the center.

    point_one = abs(x1) ** 2 + abs(y1) ** 2
    point_two = abs(x2) ** 2 + abs(y2) ** 2
    point_three = abs(x3) ** 2 + abs(y3) ** 2
    point_four = abs(x4) ** 2 + abs(y4) ** 2

    if point_one + point_two >= point_three + point_four:
        if point_one <= point_two:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    elif point_three + point_four > point_one + point_two:
        if point_three <= point_four:
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

final_result = longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
print(final_result)