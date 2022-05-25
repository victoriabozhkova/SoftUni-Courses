goal = 10000
input_line = input()
steps_count = 0

while input_line != "Going home":
    steps = int(input_line)
    steps_count += steps

    if steps_count >= goal:
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    steps_count += steps_home

diff = steps_count - goal
if steps_count >= goal:
    print("Goal reached! Good job!")
    print(f"{steps_count - goal} steps over the goal!")
else:
    print(f"{goal - steps_count} more steps to reach goal.")
