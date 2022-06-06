string = input()
string = string.lower()

my_list = ["water", "sand", "sun", "fish"]

word_count = 0

for item in my_list:
    if item in string:
        # .count() - колко пъти елементът се открива в листа
        word_count_txt = string.count(item)
        word_count += word_count_txt

print(word_count)
