current_letter = input()
save_letter = ""
secret_letter_counter = 0
secret_c_counter = 0
secret_o_counter = 0
secret_n_counter = 0
secret_counter_reset = 0

while current_letter != "End":
    if current_letter == "c":
        secret_c_counter += 1
        if secret_c_counter > 1:
            save_letter += current_letter
    elif current_letter == "o":
        secret_o_counter += 1
        if secret_o_counter > 1:
            save_letter += current_letter
    elif current_letter == "n":
        secret_n_counter += 1
        if secret_n_counter > 1:
            save_letter += current_letter
    elif not current_letter.isalpha():
        pass
    else:
        save_letter += current_letter

    if secret_n_counter > 0 and secret_o_counter > 0 and secret_c_counter > 0:
        secret_letter_counter += 1
        save_letter += " "
        print(save_letter, end = "")

        secret_c_counter = 0
        secret_o_counter = 0
        secret_n_counter = 0
        save_letter = ""

    current_letter = input()
