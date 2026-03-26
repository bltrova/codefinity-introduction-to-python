grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
    
}
egg_details = grocery_inventory.get("Eggs")
if egg_details[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    egg_category, egg_price, egg_stock = grocery_inventory["Eggs"]
    new_price = egg_price - 1
    grocery_inventory["Eggs"] = (egg_category, new_price, egg_stock)
else:
    print("The price of Eggs is reasonable")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_details = grocery_inventory.get("Milk")
if milk_details[2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
    new_stock = milk_stock + 20
    grocery_inventory["Milk"] = (milk_category, milk_price, new_stock)
else:
    print("Milk has sufficient stock.")
apples_details = grocery_inventory.get("Apples")
if apples_details[1] > 2:
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)