prices = [29.99, 45.50, 12.75, 38.20]

for cost in range(len(prices)):
    if cost == 0:
        prices[cost] -= prices[cost] * 0.10
    elif cost == 1:
        prices[cost] -= prices[cost] * 0.20
    elif cost == 2:
        prices[cost] -= prices[cost] * 0.15
    elif cost == 3:
        prices[cost] -= prices[cost] * 0.05

    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")