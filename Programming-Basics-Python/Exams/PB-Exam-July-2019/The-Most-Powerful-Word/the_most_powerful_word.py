import sys
import math
command_line = input()
words_points = - sys.maxsize
winner = ""

while command_line != "End of words":
    current_word = command_line
    current_points = 0
    for i in range(len(current_word)):
        current_letter = current_word[i]
        current_points += ord(current_letter)
        if current_word[i] == chr(92):
            current_points = 39
    if current_word[0] == "a" or current_word[0] == "A":
        current_points *= len(current_word)
    elif current_word[0] == "e" or current_word[0] == "E":
        current_points *= len(current_word)
    elif current_word[0] == "i" or current_word[0] == "I":
        current_points *= len(current_word)
    elif current_word[0] == "o" or current_word[0] == "O":
        current_points *= len(current_word)
    elif current_word[0] == "u" or current_word[0] == "U":
        current_points *= len(current_word)
    elif current_word[0] == "y" or current_word[0] == "Y":
        current_points *= len(current_word)
    else:
        current_points /= len(current_word)

    if current_points > words_points:
        words_points = current_points
        winner = command_line
    command_line = input()

print(f"The most powerful word is {winner} - {math.floor(words_points)}")


