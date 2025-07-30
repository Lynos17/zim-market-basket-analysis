import random
import csv
from datetime import datetime, timedelta

# Common FMCG grocery items
products = [
    ('Tea Bags 100g', 1.20), ('Green Bar Soap', 1.00), ('Milk 1L', 1.60), ('Sugar 2kg', 2.50), ('Cooking Oil 2L', 2.00), ('Mealie Meal 10kg', 6.00),
    ('Salt 500g', 0.50), ('Rice 2kg', 1.60), ('Margarine 250g', 2.00), ('Cerevita 500g', 3.50), ('Spaghetti 500g', 1.00), ('Bathing Soap 175g', 1.00),
    ('Matches (Box)', 0.10), ('Toilet Paper', 2.00), ('Dishwashing Liquid 750ml', 1.50), ('Scouring Powder 500g', 1.50), ('Flour 2kg', 2.50),
    ('Kapenta 150g', 1.00), ('Tea Leaves 150g', 1.00), ('Peanut Butter 1L', 2.50), ('Peanut Butter 375ml', 1.50), ('Chilli Sauce', 1.00),
    ('Margarine 500g', 2.00), ('Body Spray 200ml', 3.00), ('Coca-Cola 500ml', 0.60), ('Pepsi 500ml', 0.45), ('Sprite 500ml', 0.60), ('Mayonnaise', 2.00),
    ('Fanta Orange 500ml', 0.50), ('Water 750ml', 0.30), ('Energy Drink 400ml', 0.60), ('Chocolate Bar', 0.80), ('Sour Candies', 0.85),
    ('Toothpaste 100ml', 1.00), ('Roll On 50ml', 2.00), ('Macaroni 2kg', 3.00), ('Macaroni 3kg', 4.00), ('Domestos 750ml', 2.00), ('Eggs crate', 4.00),
    ('Powdered Soup Mix Box', 3.00), ('Pop Corn 500g', 1.00), ('Mazoe 2L', 4.00), ('Body Cream 250ml', 3.00), ('Biscuits 500g', 2.00),
    ('Vaseline 100ml', 1.00), ('Painkillers (blister)', 0.30), ('Body Cream 250ml', 3.00), ('Instant Noodles (5 packets)', 1.00), ('Jam 375ml', 1.00),
    ('Steel Wool 4 pieces', 0.50), ('Biscuits 2kg', 5,50), ('Sweets (assorted)', 0.10), ('Sanitary Pads (pack)', 2.00), ('Mealie Meal 5kg', 3.50)
    ]


# Set parameters (number of transactions and start date)
num_transactions = 9000 # Month of May data
start_date = datetime(2025, 5, 1)
transactions = []

# Generate simulated transactions
for tx_id in range(1, num_transactions + 1):
    date = start_date + timedelta(days=random.randint(0, 31))  # Random date in May
    basket_size = random.randint(1, 10)  # Each basket has 1 to 10 different items
    selected_items = random.sample(products, basket_size)

    for item in selected_items:
        quantity = random.randint(1, 3)  # Quantity bought of that item
        transactions.append({
            "Transaction ID": f"T{tx_id:04d}",
            "Date": date.strftime('%d-%m-%Y'),
            "Item": item,
            "Quantity": quantity
        })


# Save to CSV
with open("fmcg_cbd_shop_data.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Transaction ID", "Date", "Item", "Quantity"])
    writer.writeheader()
    writer.writerows(transactions)

print("✅ CSV file created: fmcg_cbd_shop_data.csv")
