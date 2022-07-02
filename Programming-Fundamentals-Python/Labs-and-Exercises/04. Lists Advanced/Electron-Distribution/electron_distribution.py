number_of_electrons = int(input())

shell_position = 0
electrons_left = number_of_electrons
list_of_shells = []
while True:
    shell_position +=1
    max_electrons_in_a_shell = 2 * shell_position ** 2
    if electrons_left > max_electrons_in_a_shell:
        electrons_left -= max_electrons_in_a_shell
        list_of_shells.append(max_electrons_in_a_shell)
    else:
        list_of_shells.append(electrons_left)
        break

print(list_of_shells)



