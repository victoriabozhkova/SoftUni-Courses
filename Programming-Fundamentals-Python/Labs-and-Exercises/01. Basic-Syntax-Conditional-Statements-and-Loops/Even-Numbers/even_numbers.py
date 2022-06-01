number = int(input())

for i in range(0, number):
    input_number = int(input())

    if input_number % 2 != 0:
        print(f"{input_number} is odd!")
        break
    else:
        pass
else:
    print("All numbers are even.")