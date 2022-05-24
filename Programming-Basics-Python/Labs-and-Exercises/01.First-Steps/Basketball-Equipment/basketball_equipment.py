yearly_fee = int(input())

shoes = yearly_fee - yearly_fee * 0.4
equipment = shoes - shoes * 0.2
ball = equipment / 4
accessories = ball / 5

final_price = shoes + equipment + ball + accessories + yearly_fee
print(final_price)

