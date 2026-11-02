
print("--- Exercise 1 ---")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--- Exercise 2 ---")
customer['phone'] = '555-5555'
print(customer)
customer['tier']   = 'platinum'
print(customer)
del customer['name']
print(customer)

print(customer.get('ytd_spend',0))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])


print("---Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
       "silver": 0.5,
        "gold": 0.1,
        "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


print("--- Exercise 6 --- ")

customers= [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")


print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")


print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)




# Reflection Questions

# Question 1: I would use .get() when a key might be missing so my code does not crash. I would use brackets when I know the key exists and want its value.

# Question 2: This reminds me of adding up sales in Excel based on different regions. Python is more useful for the larger datasets because it can organize it quicker.