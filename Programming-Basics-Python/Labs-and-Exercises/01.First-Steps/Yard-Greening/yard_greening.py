area = float(input())

price_per_metre = 7.61
final_price = area * price_per_metre
discount = 0.18 * final_price

price_w_discount = final_price - discount

print(f"The final price is: {price_w_discount:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")






