bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoins_to_lv = bitcoin * 1168
chinese_yuan_to_usd = chinese_yuan * 0.15
usd_to_lv = chinese_yuan_to_usd * 1.76
lv_to_euro = (bitcoins_to_lv + usd_to_lv) / 1.95

final_price_w_commission = lv_to_euro * (100 - commission) /100
print(f"{final_price_w_commission:.2f}")