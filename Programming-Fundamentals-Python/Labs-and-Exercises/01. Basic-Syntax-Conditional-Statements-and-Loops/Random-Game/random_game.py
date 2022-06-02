import random

theme = ["history", "math", "geography"]

history_questions = ["When did WW2 start?", "When was John F. Kennedy shot?",
                     "When was Bulgaria occupied by the Ottoman Empire?"]

math_questions = ["What's 4 x 8?", "How many cm are in a metre?", "Which number you can't divide by?"]

geography_questions = ["Where is Budapest?", "Which is the northern border of Greece?", "What is the capital of Spain?"]

right_answers = 0
wrong_answers = 0
player_theme_pick = input("Choose a theme: history, math or geography.\n")
if player_theme_pick == "history":
    for i in range(3):
        question = random.choice(history_questions)
        print(question)
        player_answer = input("Your answer: ")
        if question == "When did WW2 start?":
            right_answer = "1939"
        elif question == "When was John F. Kennedy shot?":
            right_answer = "1963"
        elif question == "When was Bulgaria occupied by the Ottoman Empire?":
            right_answer = "1396"
        if player_answer == right_answer:
            right_answers += 1
        else:
            wrong_answers += 1
        history_questions.remove(question)

if player_theme_pick == "math":
    for i in range(3):
        question = random.choice(math_questions)
        print(question)
        player_answer = input("Your answer: ")
        if question == "What's 4 x 8?":
            right_answer = "32"
        elif question == "How many cm are in a metre?":
            right_answer = "100"
        elif question == "Which number you can't divide by?":
            right_answer = "0"
        if player_answer == right_answer:
            right_answers += 1
        else:
            wrong_answers += 1
        math_questions.remove(question)

if player_theme_pick == "geography":
    for i in range(3):
        question = random.choice(geography_questions)
        print(question)
        player_answer = input("Your answer: ")
        if question == "Where is Budapest?":
            right_answer = "Hungary"
        elif question == "Which is the northern border of Greece?":
            right_answer = "Bulgaria"
        elif question == "What is the capital of Spain?":
            right_answer = "Madrid"
        if player_answer == right_answer:
            right_answers += 1
        else:
            wrong_answers += 1
        geography_questions.remove(question)

print("Game over!")
print(f"You got: {right_answers} right answers")
print(f"You got: {wrong_answers} wrong answers")

if right_answers > wrong_answers:
    print("You won!")
else:
    print("You lost!")



