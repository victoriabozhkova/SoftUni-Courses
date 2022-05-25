period_of_time = int(input())
doctors = 7
pregledani = 0
nepregledani = 0
for current_day in range(1, period_of_time+1):
    number_of_patients = int(input())
    if current_day % 3 == 0:
        if nepregledani > pregledani:
            doctors = doctors + 1

    if number_of_patients <= doctors:
        pregledani = pregledani + number_of_patients
    if number_of_patients > doctors:
        nepregledani = nepregledani + number_of_patients - doctors
        pregledani = pregledani + doctors


print(f"Treated patients: {pregledani}.")
print(f"Untreated patients: {nepregledani}.")

