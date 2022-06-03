number = int(input())
message = ""
for i in range(1, number + 1):
    code = int(input())
    if code == 88:
        message = "Hello"
    elif code == 86:
        message = "How are you?"
    elif code < 88 and code != "86":
        message = "GREAT!"
    elif code > 88:
        message = "Bye."
    print(message)