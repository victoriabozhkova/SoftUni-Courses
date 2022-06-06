str = input()

list = str.split(", ")

list.append("my_position")

my_position = len(list) - 1
wolf_position = 0

for index, wolf in enumerate(list):
    if wolf == "wolf":
        wolf_position = index

if list[-2] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {my_position-wolf_position-1}! You are about to be eaten by a wolf!" )


