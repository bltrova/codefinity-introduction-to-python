# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for items, details in inventory.items():
    current_stock = details[0]
    min_stock = details[1]
    rest_qty = details[2]
    on_sale = details[3]
    print("Processing", items)

    while current_stock < min_stock:
        current_stock += rest_qty
        inventory[items][0] = current_stock

    if current_stock > discount_threshold and not details[3]:
        details[3] = True
    
    print("Processing completed")