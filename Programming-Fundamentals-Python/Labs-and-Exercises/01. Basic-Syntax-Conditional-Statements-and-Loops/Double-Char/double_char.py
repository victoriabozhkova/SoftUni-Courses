command = input()


while command != "End":
    word = command
    new_word = ""
    if word == "SoftUni":
        pass
    else:
        for i in range(len(word)):
            new_word += word[i] * 2
        print(new_word)

    command = input()