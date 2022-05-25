x = float(input())
y = float(input())
h = float(input())

front_walls = 2 * x * x - 2 * 1.2
side_walls = 2 * x *y - 2 * 1.5 * 1.5
front_and_side_walls = front_walls + side_walls
green_paint = front_and_side_walls / 3.4

ceiling = 2 * x * y + 2 * x * h / 2
red_paint = ceiling / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
