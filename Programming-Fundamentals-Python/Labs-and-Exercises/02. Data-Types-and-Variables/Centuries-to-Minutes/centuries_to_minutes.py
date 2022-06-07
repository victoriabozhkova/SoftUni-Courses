from math import floor
centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {floor(years)} years = {floor(days)} days = {floor(hours)} hours = {floor(minutes)} minutes")