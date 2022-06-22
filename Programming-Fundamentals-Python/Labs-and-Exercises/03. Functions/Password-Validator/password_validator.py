def valid_length(text):
    if 6 <= len(text) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def characters_and_digits_only(text):
    if text.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def at_least_two_digits(text):
    digits_count = 0
    for symbol in text:
        if symbol.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()

validated = [valid_length(password), characters_and_digits_only(password), at_least_two_digits(password)]
if all(validated):
    print("Password is valid")