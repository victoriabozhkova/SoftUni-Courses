season = input()
group = input()
students = int(input())
nights = int(input())
price_nights = float()
sport = str()
discount = 0
final_price = 0

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
        price_nights = nights * 9.6 * students
    if group == "boys":
        sport = "Judo"
        price_nights = nights * 9.6 * students
    if group == "mixed":
        sport = "Ski"
        price_nights = nights * 10 * students
elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
        price_nights = nights * 7.2 * students
    if group == "boys":
        sport = "Tennis"
        price_nights = nights * 7.2 * students
    if group == "mixed":
        sport = "Cycling"
        price_nights = nights * 9.5 * students
elif season == "Summer":
    if group == "girls":
        sport = "Volleyball"
        price_nights = nights * 15 * students
    if group == "boys":
        sport = "Football"
        price_nights = nights * 15 * students
    if group == "mixed":
        sport = "Swimming"
        price_nights = nights * 20 * students

if students >= 50:
    discount = 0.5 * price_nights
elif 20 <= students < 50:
    discount = 0.15 * price_nights
elif 10 <= students < 20:
    discount = 0.05 * price_nights

final_price = price_nights - discount

print(f"{sport} {final_price:.2f} lv.")