integer = int(input())


for first_chr in range(97, 97 + integer):
    for sec_chr in range(97, 97 + integer):
        for third_chr in range(97, 97 +  integer):
            print(chr(first_chr) + chr(sec_chr) + chr(third_chr))