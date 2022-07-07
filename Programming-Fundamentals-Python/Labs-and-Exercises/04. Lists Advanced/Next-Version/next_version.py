current_version = input()
current_version = current_version.replace(".", "")

new_version = int(current_version) + 1
new_version_list = [str(x) for x in str(new_version)]


if int(new_version_list[1]) > 9:
    new_version_list[1] = 0
    new_version_list[0] = int(new_version_list[0]) + 1
elif int(new_version_list[2]) > 9:
    new_version_list[2] = 0
    new_version_list[1] = 0

print(".".join(new_version_list))