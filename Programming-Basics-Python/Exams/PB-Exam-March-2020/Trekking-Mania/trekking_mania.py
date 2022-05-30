number_of_groups = int(input())
mussala_group = 0
montblanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
sum_people = 0

for i in range(1, number_of_groups + 1):
    people_in_a_group = int(input())
    sum_people += people_in_a_group

    if people_in_a_group <= 5:
        mussala_group += people_in_a_group
    elif 6 <= people_in_a_group <= 12:
        montblanc_group += people_in_a_group
    elif 13 <= people_in_a_group <= 25:
        kilimanjaro_group += people_in_a_group
    elif 26 <= people_in_a_group <= 40:
        k2_group += people_in_a_group
    elif people_in_a_group >= 41:
        everest_group += people_in_a_group

mussala_percent = mussala_group / sum_people * 100
montblanc_percent = montblanc_group / sum_people * 100
kilimanjaro_percent = kilimanjaro_group / sum_people * 100
k2_percent = k2_group / sum_people * 100
everest_percent = everest_group / sum_people * 100

print(f"{mussala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")




