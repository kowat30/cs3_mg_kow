def calculate_total(topping_count):
    topping_price = 1.50
    total_topping_price = topping_count * topping_price
    base_price = 10.00
    total_price = base_price + total_topping_price
    return total_price
topping_count = 0

while True:
    topping = input(
        "What topping do you want? (Type 'done' to finish): "
    )
    if topping == "done":
        break
    topping_count += 1
total = calculate_total(topping_count)

discount_code = input("Do you have a discount code? click enter if none ").strip()
if discount_code == "PYTHON20":
    total *= 0.80
else: print("discount code invalid")
    
print(f'Final total = ${total:.2f}')
    

