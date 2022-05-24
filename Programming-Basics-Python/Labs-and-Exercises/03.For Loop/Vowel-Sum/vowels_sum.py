
some_text = input()
length = len(some_text)
points = 0

for current_index in range(length):
    if some_text[current_index] == "a":
        points += 1
    elif some_text[current_index] == "e":
        points += 2
    elif some_text[current_index] == "i":
        points += 3
    elif some_text[current_index] == "o":
        points += 4
    elif some_text[current_index] == "u":
        points += 5

print(points)



