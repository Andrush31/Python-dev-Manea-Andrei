# ---------------------
# Task 4
# ---------------------
import pandas as pd
import sqlite3

conn = sqlite3.connect('./magazin_data.db')

# 1. Cei mai activi clienti(top 10 clienti dupa numarul de comenzi)
df_orders = pd.read_sql('SELECT * FROM orders', conn)
df_customers = pd.read_sql('SELECT customer_id, name FROM customers', conn)

top_clients = df_orders['customer_id'].value_counts().head(10).reset_index()
top_clients.columns = ['customer_id', 'order_count']
top_clients_df = top_clients.merge(df_customers, on='customer_id', how='left')
top_clients_df = top_clients_df[['customer_id', 'name', 'order_count']]

print("Top 10 cei mai activi clienți după numărul de comenzi:")
print(top_clients_df)

conn.close()

# 2. Produsele cu cele mai multe recenzii
top_reviewed_products = reviews['product_id'].value_counts().head(10)

top_reviewed_products_df = top_reviewed_products.reset_index()
top_reviewed_products_df.columns = ['product_id', 'review_count']

print("Produsele cu cele mai multe recenzii:")
print(top_reviewed_products_df)

# 3. Categoriile cu cele mai multe vanzari in functie de cantitate
merged_data = pd.merge(orders, products, on='product_id')

category_sales = merged_data.groupby('category')['quantity'].sum().sort_values(ascending=False)

category_sales_df = category_sales.reset_index()
category_sales_df.columns = ['category', 'total_quantity_sold']

print("Categoriile cu cele mai multe vânzări în funcție de cantitate:")
print(category_sales_df)
