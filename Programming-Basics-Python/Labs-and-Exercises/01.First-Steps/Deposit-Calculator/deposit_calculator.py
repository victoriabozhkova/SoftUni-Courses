deposit = float(input())
months = int(input())
yearly_interest = float(input())

per_year = deposit * (yearly_interest/100)
per_month = per_year / 12
total_sum = deposit + (months * per_month)
print(total_sum)

