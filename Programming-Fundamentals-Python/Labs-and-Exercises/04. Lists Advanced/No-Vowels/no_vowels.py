text = input()
vowels_list = ["a", "e", "i", "o", "u"]
new_text = [letter for letter in text if letter not in vowels_list]
print(*new_text, sep='')