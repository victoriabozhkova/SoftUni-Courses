packages = int(input())
price = 0
sum_tons = 0
average_per_ton = 0
with_microbus_count = 0
with_truck_count = 0
with_train_count = 0
microbus_percent = 0
truck_percent = 0
train_percent = 0
for package_count in range(1, packages + 1):
    package_weight = int(input())

    sum_tons = sum_tons + package_weight

    if package_weight <= 3:
        price = price + 200 * package_weight
        with_microbus_count = with_microbus_count + package_weight
    elif 4 <= package_weight <= 11:
        price = price + 175 * package_weight
        with_truck_count = with_truck_count + package_weight
    elif 12 <= package_weight:
        price = price + 120 * package_weight
        with_train_count = with_train_count + package_weight

average_per_ton = price / sum_tons

microbus_percent = with_microbus_count / sum_tons * 100
truck_percent = with_truck_count / sum_tons * 100
train_percent = with_train_count / sum_tons * 100

print(f"{average_per_ton:.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")

