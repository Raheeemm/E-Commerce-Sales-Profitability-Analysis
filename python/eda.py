import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/cleaned/superstore_clean.csv")

# Overall business numbers

total_sales=df["sales"].sum()
print("Total Sales : ",total_sales)

total_quantity=df['quantity'].sum()
print("Total quantity : ",total_quantity)

total_profit=df['profit'].sum()
print("Total Profit : ",total_profit)

profit_margin=total_profit/total_sales
print(f"Profit margin : {profit_margin:.2%}")

'''
# Category performance

category_analysis=(
    df.groupby("category")
    .agg(
        sales=("sales","sum"),
        profit=("profit","sum"),
        quantity=("quantity","sum")
    )
    .sort_values("sales",ascending=False)
)

category_analysis["profit_margin"]=(category_analysis["profit"]/category_analysis["sales"])
print(category_analysis)


# Visualizing category analysis

category_analysis['sales'].plot(
    kind='bar',
    title='Sales by Category'
)
plt.ylabel("Sales")
plt.tight_layout
plt.show()

category_analysis['profit'].plot(
    kind='bar',
    title='Profit by Category'
)
plt.ylabel("Profit")
plt.tight_layout
plt.show()


# Sub category analysis

subcategory_analysis=(
    df.groupby("sub_category")
    .agg(
        sales=('sales','sum'),
        profit=('profit','sum'),
        quantity=('quantity','sum')
    )
    .sort_values('profit',ascending=False)
)
print(subcategory_analysis.sort_values('sales',ascending=False).head(10))
print(subcategory_analysis.sort_values('profit',ascending=False).head(10))
print(subcategory_analysis.sort_values('profit').head(10))

loss_making=subcategory_analysis[subcategory_analysis['profit']<0]
print(loss_making)


#Regional analysis

region_analysis = (
    df.groupby("region")
      .agg(
          sales=("sales", "sum"),
          profit=("profit", "sum"),
          quantity=("quantity", "sum")
      )
      .sort_values("sales", ascending=False)
)

region_analysis["profit_margin"] = (
    region_analysis["profit"] /
    region_analysis["sales"]
)

print(region_analysis)


# Segment analysis

segment_analysis=(
    df.groupby("segment")
    .agg(
        sales=('sales','sum'),
        profit=('profit','sum'),
        quantity=('quantity','sum')
    )
    .sort_values('sales',ascending=False)
)
segment_analysis['profit_margin']=(segment_analysis['profit']/segment_analysis['sales'])
print(segment_analysis)


# Discount analysis

discount_analysis = (
    df.groupby("discount")
      .agg(
          sales=("sales", "sum"),
          profit=("profit", "sum"),
          quantity=("quantity", "sum")
      )
      .sort_index()
)

discount_analysis["profit_margin"] = (
    discount_analysis["profit"] /
    discount_analysis["sales"]
)

print(discount_analysis)

plt.scatter(
    df['discount'],
    df['profit'],
    alpha=0.4
)
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.title('Discount vs Profit')
plt.tight_layout
plt.show()'''

losses=df[df["profit"]<0]
losses[
    [
        "category",
        "sub_category",
        "region",
        "segment",
        "sales",
        "discount",
        "profit"
    ]
].sort_values("profit")
print(losses)

summary=(
    df.groupby(['region','category'])
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        quantity=("quantity", "sum")
    )
    .reset_index()
)
summary['profit_margin']=(summary['profit']/summary['sales'])

print(summary)