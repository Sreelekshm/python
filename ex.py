import pandas as pd 
import matplotlib.pyplot as plt
df =pd.read_csv("retail_sales_exact_columns.csv")

print(df.head(10))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Average Sales:", df["Sales"].mean())
print("Highest Sales:", df["Sales"].max())
print("Lowest Sales:", df["Sales"].min())       


plt.scatter(df["Sales"], df["Profit"],
            marker="D", s=50)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()

print("Correlation:",
      df["Sales"].corr(df["Profit"]))



region_sales = df.groupby("Region")["Sales"].sum()

# Vertical bar chart
plt.bar(region_sales.index, region_sales.values)

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()




plt.barh(region_sales.index, region_sales.values)

plt.title("Region-wise Sales")
plt.xlabel("Sales")
plt.ylabel("Region")

plt.show()

print("Highest Sales Region:",
      region_sales.idxmax())

print("Lowest Sales Region:",
      region_sales.idxmin())





product_sales = df.groupby("Product")["Sales"].sum()

explode = [0.1 if x == product_sales.idxmax()
           else 0 for x in product_sales.index]

plt.pie(product_sales.values,
        labels=product_sales.index,
        autopct="%1.1f%%",
        explode=explode,
        startangle=90)

plt.title("Product Sales Contribution")

plt.show()





plt.hist(df["Customer Age"], bins=5,
         edgecolor="black")

plt.title("Customer Age Distribution")
plt.xlabel("Customer Age")
plt.ylabel("Frequency")

plt.show()

# 10 bins
plt.hist(df["Customer Age"], bins=10,
         edgecolor="black")

plt.title("Customer Age Distribution - 10 Bins")
plt.xlabel("Customer Age")
plt.ylabel("Frequency")

plt.show()




plt.boxplot(df["Profit"])

plt.title("Profit Distribution")
plt.ylabel("Profit")

plt.show()

# Calculate Q1, Q3 and IQR
Q1 = df["Profit"].quantile(0.25)
Q3 = df["Profit"].quantile(0.75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Identify possible outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Profit"] < lower) |
    (df["Profit"] > upper)
]

print("Possible Outliers:")
print(outliers)




region_data = df.groupby("Region")[["Sales", "Profit"]].sum()

print(region_data)

region_data.plot(kind="bar")

plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount")

plt.show()




product_profit = df.groupby("Product")["Profit"].sum()

print("Most Profitable Product:",
      product_profit.idxmax())



category_sales = df.groupby("Category")["Sales"].sum()

selected = category_sales.loc[
    ["Electronics", "Accessories"]
]

plt.bar(selected.index, selected.values)

plt.title("Electronics vs Accessories")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()