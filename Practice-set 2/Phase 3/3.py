orders = [
    {"customer_id": 101, "item": "Laptop"},
    {"customer_id": 102, "item": "Mouse"},
    {"customer_id": 101, "item": "Keyboard"},
    {"customer_id": 103, "item": "Monitor"},
    {"customer_id": 102, "item": "USB Cable"}
]

grouped_orders = {}

for order in orders:
    cid = order["customer_id"]
    item = order["item"]
    
    if cid not in grouped_orders:
        grouped_orders[cid] = []
        
    grouped_orders[cid].append(item)

print(grouped_orders)