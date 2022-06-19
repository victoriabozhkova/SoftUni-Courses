
def add_ands_subtract(a, b, c):
    def sum_numbers(a, b):
        return a + b


    def subtract(a, b):
        return a - b

    first_result = sum_numbers(number_1, number_2)
    second_result = subtract(first_result, number_3)
    return second_result

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
final_result = add_ands_subtract(number_1, number_2, number_3)
print(final_result)
