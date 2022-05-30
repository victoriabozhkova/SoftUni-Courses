record_in_sec = float(input())
distance_in_m = float(input())
metres_in_sec = float(input())

import math

delay = math.floor(distance_in_m / 50) * 30

his_record = distance_in_m * metres_in_sec + delay

if his_record >= record_in_sec:
    print(f"No! He was {his_record - record_in_sec:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {his_record:.2f} seconds.")

