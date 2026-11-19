
import seaborn as sns

# ==== Part 1 Count plot ====

# ---- Q1. Regional Order Analysis ----

# sns.countplot(x=df['Region'])
# plt.title('Regional Order Analysis')
# plt.show()

# ---- Q2. Product Category Distribution ----

# sns.countplot(x=df['Category'])
# plt.title('Product Category Distribution')
# plt.show()

# ==== Part 2 – Bar Plot ====

# ---- Q3. Regional Sales Performance ----

# sns.barplot(x=df['Region'],y=df['Sales'])
# plt.title('Regional Sales Performance')
# plt.show()

# ---- Q4. Product Profitability Analysis ----

# sns.barplot(x=df['Profit'],y=df['Product'])
# plt.title('Product Profitability Analysis')
# plt.show()

# ==== Part 3 – Line Plot ====

# ---- Q5. Monthly Revenue Analysis ----

# sns.lineplot(x=df['Sales'],y=df['Month_Name'])
# plt.title('Monthly Revenue Analysis')
# plt.show()

# ---- Q6. Monthly Profit Analysis ----

# sns.lineplot(x=df['Month_Name'],y=df['Profit'])
# plt.title('Monthly Profit Analysis')
# plt.show()

# ==== Part 4 – Correlation and Heatmap ====

# ---- Q7. Business Correlation Analysis ----

# corr = df.corr(numeric_only=True)
# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.title('Business Correlation Analysis')
# plt.show()

# ==== Part 5 – Pairplot ====

# ---- Q8. Sales and Profit Relationship Analysis ----

# sns.pairplot(df[['Sales','Profit','Quantity','Unit Price']])
# plt.title('Sales and Profit Relationship Analysis')
# plt.show()

# ==== Part 6 – Hue Parameter ====

# ---- Q9. Regional Category Performance ----

# sns.countplot(x=df['Region'],hue=df['Category'])
# plt.title('Regional Category Analysis')
# plt.xlabel('Region')
# plt.ylabel('Count of product')
# plt.show()

# ---- Q10. Regional Profit Comparison ----

# sns.barplot(x=df['Region'],y=df['Profit'],hue=df['Category'])
# plt.title('Regional profit Comparison')
# plt.xlabel('Region')
# plt.ylabel('Average of profit')
# plt.show()