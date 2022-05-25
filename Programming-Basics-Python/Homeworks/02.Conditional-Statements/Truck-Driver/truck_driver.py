season = input()
km_per_month = float(input())
monthly_salary = 0
final =0

if km_per_month <= 5000:
    if season == "Spring" or "Autumn":
        monthly_salary = km_per_month * 0.75
    if season == "Summer":
        monthly_salary= 0.9 * km_per_month
    if season == "Winter":
        monthly_salary = 1.05 * km_per_month
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or "Autumn":
        monthly_salary = 0.95 * km_per_month
    if season == "Summer":
        monthly_salary = 1.1 * km_per_month
    if season == "Winter":
        monthly_salary = 1.25 * km_per_month
elif 10000 < km_per_month <= 20000:
    monthly_salary = 1.45 * km_per_month

final = monthly_salary * 4
tax = final * 0.1

print(f"{final - tax:.2f}")




