prices = []
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

budget = int(input("Enter total budget: "))

current_total = 0
bought_items = []

for i in range(len(prices)):
    item_price = prices[i]
    
    if current_total + item_price <= budget:
        print(f"Item {i + 1} = {item_price} -> buy")
        current_total += item_price
        bought_items.append(item_price)
    else:
        print(f"Item {i + 1} = {item_price} -> cannot buy")
        
    print(f"Current total = {current_total}")

remaining_budget = budget - current_total
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")