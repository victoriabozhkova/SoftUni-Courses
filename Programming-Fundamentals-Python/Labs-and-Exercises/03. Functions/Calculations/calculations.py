def operation(number_a, number_b):
    result = 0
    if given_operation == "multiply":
        result = number_a * number_b
    elif given_operation == "divide":
        result = number_a / number_b
    elif given_operation == "add":
        result = number_a + number_b
    elif given_operation == "subtract":
        result = number_a - number_b
    return result


given_operation = input()
number_a = int(input())
number_b = int(input())
print(int(operation(number_a, number_b)))