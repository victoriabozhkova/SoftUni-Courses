sequence = input().split()

for message in sequence:
    symbols = [x for x in message]
    digits = [x for x in message if x.isdigit()]
    first_letter_number = ''.join(digits)
    first_letter = int(first_letter_number)

    letters = [x for x in symbols if x.isalpha()]
    letters.append(letters[0])
    letters[0] = letters[-2]
    letters.pop(-2)
    final_letters = ''.join(letters)

    final_word = chr(first_letter) + final_letters
    print(final_word, end=' ')