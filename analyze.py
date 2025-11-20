import pandas as pd

data = pd.read_csv('sales.csv')

print("\n==== Preview of Data ====")
print(data.head())

print("\n==== Basic Info ====")
print(data.info())

print("\n==== Summary Statistics (Numerical Columns) ====")
print(data.describe())

# Total sales amount
total_sales = data["Sales_Amount"].sum()
print("\nTotal Sales Amount:", total_sales)

# Average sales
avg_sales = data["Sales_Amount"].mean()
print("Average Sales Amount:", avg_sales)

# Highest sale
highest_sale = data.loc[data["Sales_Amount"].idxmax()]
print("\nPerson with Highest Sales:\n", highest_sale)

# Lowest sale
lowest_sale = data.loc[data["Sales_Amount"].idxmin()]
print("\nPerson with Lowest Sales:\n", lowest_sale)

# Total units sold
total_units = data["Units_Sold"].sum()
print("\nTotal Units Sold:", total_units)

# Sales by region
sales_by_region = data.groupby("Region")["Sales_Amount"].sum()
print("\n==== Sales by Region ====")
print(sales_by_region)

# Units sold by product
units_by_product = data.groupby("Product")["Units_Sold"].sum()
print("\n==== Units Sold by Product ====")
print(units_by_product)

# Sales by product
sales_by_product = data.groupby("Product")["Sales_Amount"].sum()
print("\n==== Sales by Product ====")
print(sales_by_product)