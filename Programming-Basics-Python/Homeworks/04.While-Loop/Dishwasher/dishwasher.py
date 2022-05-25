bottles_of_detergent = int(input())
command = input()
ml_in_a_bottle = 750
ml_per_plate = 5
ml_per_pot = 15
charge_count = 0
detergent_left = 0
detergent_used = 0

plates_count = 0
pots_count = 0

while command != "End":
    dishes_to_wash = int(command)
    charge_count += 1

    detergent_sum = bottles_of_detergent * ml_in_a_bottle

    if charge_count % 3 == 0:
        detergent_used = detergent_used + dishes_to_wash * ml_per_pot
        pots_count = pots_count + dishes_to_wash
    else:
        detergent_used = detergent_used + dishes_to_wash * ml_per_plate
        plates_count += dishes_to_wash

    detergent_left = detergent_left + detergent_sum - detergent_used

    if detergent_used > detergent_sum:
        break

    command = input()

if detergent_used > detergent_sum:
    print(f"Not enough detergent, {abs(detergent_used-detergent_sum)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {round(detergent_sum-detergent_used)} ml.")

