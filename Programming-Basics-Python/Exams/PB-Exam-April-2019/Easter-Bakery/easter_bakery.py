flour_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
cartons_of_eggs = float(input())
yeast_packs = float(input())

sugar_price = flour_kg_price * 0.75
egg_carton_price = flour_kg_price * 1.1
yeast_pack_price = sugar_price * 0.2

final_price = flour_kg_price * flour_kg + sugar_price * sugar_kg + cartons_of_eggs * egg_carton_price + yeast_pack_price * yeast_packs

print(f"{final_price:.2f}")
