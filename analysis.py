import pandas as pd

# Load data
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