number = int(input())
list = []

for i in str(number):
    list.append(i)

list.sort(reverse=True)

print("".join(list))

