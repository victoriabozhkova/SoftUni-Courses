# def min_max_sum(sequence):
#     minimum = min(sequence)
#     print(f"The minimum number is {minimum}")
#     maximum = max(sequence)
#     print(f"The maximum number is {maximum}")
#     summary = sum(sequence)
#     print(f"The sum number is: {summary}")
#
#
# numbers = list(map(int, input().split(" ")))
# min_max_sum(numbers)
def min_num(sequence):
    return min(sequence)


def max_num(sequence):
    return max(sequence)


def sum_nums(sequence):
    return sum(sequence)


numbers = list([int(x) for x in input().split()])
minimum = min_num(numbers)
maximum = max_num(numbers)
sum = sum_nums(numbers)

print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {sum}")






