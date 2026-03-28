# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for items, details in inventory.items():
    current_stock = details[0]
    regular_price = details[1]
    discounted_price = details[2]

    if current_stock < 30:
        print(f"{items} need restocking.")
    elif current_stock > 100:
        print(f"{items} should be sold at the discounted price of {discounted_price}.")
    elif 30 <= current_stock <= 100:
        print(f"{items} should be sold at the regular price of {regular_price}.")




