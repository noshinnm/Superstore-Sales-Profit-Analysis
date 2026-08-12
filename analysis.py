import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print("=== OVERALL SUMMARY ===")
print(df[["Sales", "Profit", "Discount"]].describe())

print("\n=== PROFIT BY CATEGORY ===")
category_profit = df.groupby("Category")["Profit"].sum()
print(category_profit.sort_values(ascending=False))

print("\n=== PROFIT MARGIN BY CATEGORY ===")

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

category_summary["Profit Margin %"] = (
    category_summary["Profit"] / category_summary["Sales"] * 100
)

print(category_summary)

print("\n=== FURNITURE SUB-CATEGORY ANALYSIS ===")

furniture = (
    df[df["Category"] == "Furniture"]
    .groupby("Sub-Category")[["Sales", "Profit"]]
    .sum()
)

furniture["Profit Margin %"] = (
    furniture["Profit"] / furniture["Sales"] * 100
)

print(furniture.sort_values("Profit Margin %"))

print("\n=== TABLES DISCOUNT ANALYSIS ===")

tables = df[df["Sub-Category"] == "Tables"]

discount_summary = tables.groupby("Discount")[["Sales", "Profit"]].sum()

discount_summary["Profit Margin %"] = (
    discount_summary["Profit"] / discount_summary["Sales"] * 100
)

print(discount_summary)


region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

region_analysis["Profit Margin %"] = (
    region_analysis["Profit"] / region_analysis["Sales"] * 100
)

print("\nRegional Analysis:")
print(region_analysis)

region_analysis["Sales"].plot(
    kind="bar",
    title="Sales by Region"
)

plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


segment_analysis = df.groupby("Segment")[["Sales", "Profit"]].sum()

segment_analysis["Profit Margin %"] = (
    segment_analysis["Profit"] / segment_analysis["Sales"] * 100
)

print("\n=== SEGMENT ANALYSIS ===")
print(segment_analysis)

segment_analysis["Profit"].plot(
    kind="bar",
    title="Profit by Segment"
)

plt.xlabel("Segment")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

print("\n=== KEY BUSINESS FINDINGS ===")

print("1. Technology has the highest profit margin among categories.")
print("2. Furniture has a much lower overall profit margin.")
print("3. Tables are loss-making, while Furnishings are profitable.")
print("4. Higher discounts are strongly associated with lower profit margins.")
print("5. West has the highest regional profit margin.")
print("6. Home Office has the highest profit margin among customer segments.")