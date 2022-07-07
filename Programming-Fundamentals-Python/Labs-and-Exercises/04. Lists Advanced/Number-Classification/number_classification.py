def positive(nums):
    return [x for x in nums if int(x) >= 0]


def negative(nums):
    return [x for x in nums if int(x) < 0]


def even(nums):
    return [x for x in nums if int(x) % 2 == 0]


def odd(nums):
    return [x for x in nums if int(x) % 2 != 0]


numbers = input().split(", ")

positive_numbers = ", ".join(positive(numbers))
negative_numbers = ", ".join(negative(numbers))
even_numbers = ", ".join(even(numbers))
odd_numbers = ", ".join(odd(numbers))
print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")



