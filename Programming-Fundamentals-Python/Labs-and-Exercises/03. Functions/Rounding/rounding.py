numbers = list(map(float, input().split(" ")))


def round_numbers(list):
    result = [round(num) for num in list]
    return result


print(round_numbers(numbers))