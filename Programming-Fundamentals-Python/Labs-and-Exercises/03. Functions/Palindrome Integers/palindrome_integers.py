def palindrome(sequence):
    for num in sequence:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome(numbers)







