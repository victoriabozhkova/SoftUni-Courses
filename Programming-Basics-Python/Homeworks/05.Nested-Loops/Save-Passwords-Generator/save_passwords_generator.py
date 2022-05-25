position_x = int(input())
position_y = int(input())
max_passwords = int(input())
counter = 0
for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, position_x +1):
            for y in range(1, position_y +1):
                if x > position_x and y > position_y:
                    break
                counter += 1
                if counter > max_passwords:
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

                A += 1
                B += 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64
            if x > position_x and y > position_y:
                break
        break
    break





