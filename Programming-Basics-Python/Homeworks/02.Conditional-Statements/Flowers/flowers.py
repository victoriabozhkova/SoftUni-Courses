hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
bouquet = float()
arrangement = 2
if season == "Spring":
    bouquet = hrizantemi * 2 + roses * 4.1 + tulips * 2.5
elif season == "Summer":
    bouquet = hrizantemi * 2 + roses * 4.1 + tulips * 2.5
elif season == "Winter":
    bouquet = hrizantemi * 3.75 + roses * 4.5 + tulips * 4.15
elif season == "Autumn":
    bouquet = hrizantemi * 3.75 + roses * 4.5 + tulips * 4.15

if holiday == "Y":
    bouquet = bouquet + bouquet * 0.15
if holiday == "N":
    pass

if tulips >= 7 and season == "Spring":
    bouquet = bouquet - bouquet * 0.05
else: pass

if roses >=10 and season == "Winter":
    bouquet = bouquet - bouquet * 0.1
else: pass

if hrizantemi + roses + tulips >= 20:
    bouquet = bouquet - bouquet * 0.2
else:
    pass

final_price = bouquet + arrangement

print(f"{final_price:.2f}")



