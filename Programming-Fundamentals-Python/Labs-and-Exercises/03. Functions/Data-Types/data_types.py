data_type = input()
data = input()


def data_output(type, data):
    result = ''
    if type == "int":
        result = int(data) * 2
    elif type == "real":
        result = f"{float(data) * 1.5:.2f}"
    elif type == "string":
        result = "$" + data + "$"
    return result


print(data_output(data_type, data))
