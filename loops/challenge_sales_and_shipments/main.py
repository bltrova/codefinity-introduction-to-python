# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

#print(products[0][1])
# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

#print(units_sold[0][1])
# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

for i in range(len(products)):
    products[i][1] += shipment_received[i][1]
    #print(products[i])
print("Final stock levels for all products:", products)