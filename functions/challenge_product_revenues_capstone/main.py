# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = [price * quantity for price, quantity in zip(prices, quantities_sold)]
    return revenue
def formatted_output(revenues):
    for product, revenue in sorted(revenues):
        print(f"{product} has total revenue of ${revenue}")

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)

