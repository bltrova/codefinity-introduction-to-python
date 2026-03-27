# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in range(5):
    promotion = daily_promotions[day]
    weekday = weekdays[day]
    print(f"{weekday}:Promotion on {promotion}")