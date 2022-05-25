control_number = int(input())
position_counter = 0
is_password_found = False
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a*b + c*d == control_number:
                    if a<b and c>d:
                        position_counter += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if position_counter == 4:
                            is_password_found = True
                            password = f"{a}{b}{c}{d}"
if is_password_found:
    print()
    print(f"Password: {password}")
else:
    print()
    print(f"No!")


