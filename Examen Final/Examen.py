import pandas as pd
import sqlite3


conn = sqlite3.connect('./magazin_data.db')

#  Task 4.1
df_orders = pd.read_sql('SELECT * FROM orders', conn)
df_customers = pd.read_sql('SELECT customer_id, name FROM customers', conn)

top_clients = df_orders['customer_id'].value_counts().head(10).reset_index()
top_clients.columns = ['customer_id', 'order_count']
top_clients_df = top_clients.merge(df_customers, on='customer_id', how='left')
top_clients_df = top_clients_df[['customer_id', 'name', 'order_count']]

print("Top 10 cei mai activi clienți după numărul de comenzi:")
print(top_clients_df)


#  Task 4.2
df_reviews = pd.read_sql('SELECT product_id FROM reviews', conn)
df_products = pd.read_sql('SELECT product_id, product_name FROM products', conn)

top_products = df_reviews['product_id'].value_counts().head(10).reset_index()
top_products.columns = ['product_id', 'review_count']

top_products_df = top_products.merge(df_products, on='product_id', how='left')
top_products_df = top_products_df[['product_id', 'product_name', 'review_count']]

print("Top 10 produse cu cele mai multe recenzii:")
print(top_products_df)



#  Task 4.3


conn.close()