def perfect_number(num):
    divisors_sum = 0
    for digit in range(1, num):
        if num % digit == 0:
            divisors_sum += digit
    if divisors_sum == num:
        return True


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


