import matplotlib.pyplot as plot
import seaborn as sns
import pandas as pd

orders_df = pd.read_csv('orders.csv')
print(orders_df.groupby('country').size())
customers_df = pd.read_csv('customers.csv')
x = orders_df.groupby('country').size()

plot.pie(x)


plot.show()



plot.show()

def plot_country_sales(orders_df, customers_df):
    country_sales = orders_df.merge(customers_df, on="customer_id").groupby("country").size()
    country_sales.plot(kind="bar", title="Distribuția vânzărilor per țară")
    plot.show()

def plot_sales_trends(monthly_revenue):
    sns.lineplot(x="month", y="total_revenue", data=monthly_revenue)
    plot.title("Tendințe de vânzăr i sezoniere")
    plot.xticks(rotation=45)
    plot.show()




