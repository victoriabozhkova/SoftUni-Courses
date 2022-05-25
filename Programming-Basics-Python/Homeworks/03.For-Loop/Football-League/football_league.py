stadium_capacity = int(input())
all_fans = int(input())
sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0
sector_a_percent = 0
sector_b_percent = 0
sector_v_percent = 0
sector_g_percent = 0
fans_in_stadium_percent = 0
for i in range(1, all_fans+1):
    sector = input()

    if sector == "A":
        sector_a_count += 1
    elif sector == "B":
        sector_b_count += 1
    elif sector == "V":
        sector_v_count += 1
    elif sector == "G":
        sector_g_count += 1

sector_a_percent = sector_a_count / all_fans * 100
sector_b_percent = sector_b_count / all_fans * 100
sector_v_percent = sector_v_count / all_fans * 100
sector_g_percent = sector_g_count / all_fans * 100
fans_in_stadium_percent = all_fans / stadium_capacity * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{fans_in_stadium_percent:.2f}%")


