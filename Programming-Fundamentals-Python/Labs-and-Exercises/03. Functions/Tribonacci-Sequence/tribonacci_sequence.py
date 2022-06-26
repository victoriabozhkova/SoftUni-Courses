def tribonacci(num):
    next_number = 0
    sequence = [1]
    for i in range(numbers-1):
        if len(sequence) <= 2:
            next_number += sequence[i]
            sequence.append(next_number)
        elif len(sequence) > 2:
            previous_three = list(sequence[-3:])
            next_number = previous_three[-3] + previous_three[-2] + previous_three[-1]
            sequence.append(next_number)
    return sequence


numbers = int(input())

tribonacci_sequence = tribonacci(numbers)
print(*tribonacci_sequence)


