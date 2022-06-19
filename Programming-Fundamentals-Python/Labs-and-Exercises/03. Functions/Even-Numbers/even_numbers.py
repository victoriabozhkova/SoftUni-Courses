
def even_numbers(sequence):
    result = list(filter(lambda x: x % 2 ==0, sequence))
    return result


numbers = list(map(int, input().split(" ")))
print(even_numbers(numbers))






