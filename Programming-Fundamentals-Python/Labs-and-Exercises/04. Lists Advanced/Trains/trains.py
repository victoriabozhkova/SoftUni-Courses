wagons_number = int(input())
train = [0] * wagons_number


while True:
    command = input()

    if command == "End":
        break

    data = command.split(" ")
    if data[0] == "add":
        train[-1] = train[-1] + int(data[1])
    elif data[0] == "insert":
        train[int(data[1])] = train[int(data[1])] + int(data[2])
    elif data[0] == "leave":
        train[int(data[1])] = train[int(data[1])] - int(data[2])



print(train)