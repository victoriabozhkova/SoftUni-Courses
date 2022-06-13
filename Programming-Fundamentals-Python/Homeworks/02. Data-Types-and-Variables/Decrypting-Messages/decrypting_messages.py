key = int(input())
number_of_lines = int(input())
final_word = ''
for i in range(number_of_lines):
    symbol = input()
    final_word += chr(ord(symbol)+key)

print(final_word)