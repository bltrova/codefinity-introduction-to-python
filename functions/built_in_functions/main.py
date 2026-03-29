# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for name, details in products.items():
    product_price = float(details[0])
    qty_sold = int(details[1])
    
    total_sales = product_price * qty_sold
    total_sales_list.append(total_sales)

    print(f"Total sales for {name}: ${total_sales:.2f}")
    
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"\nTotal sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales:.2f}")
print(f"Maximum sales: ${max_sales:.2f}")