
length = int(input())
width = int(input())
height = int(input())
percent = int(input())

volume = length * width * height
volume_lt = volume * 0.001

percent_lt = volume_lt * percent / 100
needed_water = volume_lt - percent_lt

print(needed_water)




