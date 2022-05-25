first_pair_interval_start = int(input())
second_pair_interval_start = int(input())
difference_first_interval = int(input())
difference_second_interval = int(input())
first_is_prime = False
second_is_prime = False

for i in range(first_pair_interval_start, first_pair_interval_start+difference_first_interval+1):
    for j in range(second_pair_interval_start, second_pair_interval_start+difference_second_interval+1):
        for k in range(2, i//2):
            for l in range(2, j//2):
                if j % l == 0:
                    second_is_prime = False
                    break
                second_is_prime = True
            if i % k == 0:
                first_is_prime = False
                break
            first_is_prime = True
        if first_is_prime == True and second_is_prime == True:
            print(f"{i}{j}", end=" ")
            print()






