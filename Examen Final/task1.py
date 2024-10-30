import pandas as pd
import sqlite3

conn = sqlite3.connect('./magazin_data.db')

def clean_data(orders_df, customers_df, products_df, reviews_df):
    # Curățare date
    orders_df.dropna(inplace=True)
    customers_df.dropna(inplace=True)
    products_df.dropna(inplace=True)
    reviews_df.dropna(inplace=True)

# Citire date din tabelul 'orders' din baza de date SQLite
query = 'SELECT * FROM orders'
df_orders = pd.read_sql(query, conn)  # Trebuie să folosești obiectul de conexiune, nu un string
print(df_orders)

# Închide conexiunea la baza de date
conn.close()
