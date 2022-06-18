def grade(num):
    result = ''
    if 2.0 <= num <= 2.99:
        result = "Fail"
    elif 3.00 <= num <= 3.49:
        result = "Poor"
    elif 3.50 <= num <= 4.49:
        result = "Good"
    elif 4.50 <= num <= 5.49:
        result = "Very Good"
    elif 5.50 <= num <= 6.00:
        result = "Excellent"
    return result


grades = float(input())
print(grade(grades))