import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

faker = Faker()

def generate_sales_data(num_orders=500):
    data = []
    product_categories = ['Electronics', 'Clothing', 'Books', 'Home Goods', 'Food', 'Toys', 'Sports', 'Beauty']
    for _ in range(num_orders):
        order_date = faker.date_between(start_date='-2y', end_date='today')
        price = round(random.uniform(5.0, 500.0), 2)
        quantity = random.randint(1, 10)
        discount_percent = random.choice([0, 5, 10, 15, 20, 25])

        data.append({
            'order_id': faker.uuid4(),
            'order_date': order_date,
            'customer_id': faker.uuid4(),
            'product_category': random.choice(product_categories),
            'price': price,
            'quantity': quantity,
            'discount_percent': discount_percent
        })
    return pd.DataFrame(data)

df = generate_sales_data(num_orders=500)
print(df.head())