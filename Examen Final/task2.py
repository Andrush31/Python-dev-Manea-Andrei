import pandas as pd
import sqlite3

nume_baza_date = './magazin_data.db'
sqlite_conn = sqlite3.connect(nume_baza_date)

# Venituri lunare si sezoniere
query_orders = 'SELECT * FROM orders'
orders = pd.read_sql(query_orders, sqlite_conn)

orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
orders = orders.dropna(subset=['order_date'])
orders['revenue'] = orders['quantity'] * orders['price']
orders['year_month'] = orders['order_date'].dt.to_period('M')
monthly_revenue = orders.groupby('year_month')['revenue'].sum().reset_index()
print(monthly_revenue)

# Analiza produselor populare
query_products = 'SELECT * FROM products'
products = pd.read_sql(query_products, sqlite_conn)

popular_products = orders.groupby('product_id')['quantity'].sum().reset_index()
popular_products = popular_products.merge(products, on='product_id', how='left')
category_popular_products = popular_products.sort_values('quantity', ascending=False).drop_duplicates(subset='category')
print(category_popular_products)

# Valoarea totala a clienilor
query_customers = 'SELECT * FROM customers'
customers = pd.read_sql(query_customers, sqlite_conn)

customer_revenue = orders.groupby('customer_id')['revenue'].sum().reset_index()
customer_revenue = customer_revenue.merge(customers, on='customer_id', how='left')
print(customer_revenue)

# Recenzii și satisfacția clienților
query_reviews = 'SELECT * FROM reviews'
reviews = pd.read_sql(query_reviews, sqlite_conn)

reviews_avg_rating = reviews.groupby('product_id')['rating'].mean().reset_index()
reviews_avg_rating = reviews_avg_rating.merge(products, on='product_id', how='left')
print(reviews_avg_rating)

# Top 5 clienți fideli
top_5_customers = orders['customer_id'].value_counts().head(5).reset_index()
top_5_customers.columns = ['customer_id', 'num_orders']
top_5_customers = top_5_customers.merge(customers, on='customer_id', how='left')
print(top_5_customers)
