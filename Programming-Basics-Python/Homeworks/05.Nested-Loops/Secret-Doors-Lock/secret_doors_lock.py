first_digit_max = int(input())
second_digit_max = int(input())
third_digit_max = int(input())

for i in range (1, first_digit_max + 1):
    for j in range(1, second_digit_max + 1):
        for k in range(1, third_digit_max + 1):
            if i % 2 == 0 and k % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j ==7:
                    print(f"{i} {j} {k}", end="")
                    print()