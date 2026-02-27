products = {
    1: {"price": 100, "category": "Electronics"},
    2: {"price": 40, "category": "Fashion"},
    3: {"price": 80, "category": "Fashion"},
    4: {"price": 120, "category": "Groceries"}
}

updated_products = {
    pid: {
        **details,
        "price": (
            details["price"] * 0.85 if details["category"] == "Electronics" and details["price"] > 50
            else details["price"] * 0.90 if details["category"] == "Fashion" and details["price"] > 50
            else details["price"]
        )
    }
    for pid, details in products.items()
}

print(updated_products)