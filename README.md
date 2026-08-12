# Superstore Sales & Profitability Analysis

## Project Overview

This project analyzes the Sample Superstore dataset to identify patterns in sales, profitability, profit margins, and discounting.

The goal is to understand which product categories and sub-categories contribute most to profitability and identify areas where discounts may be associated with lower profits.

## Tools Used

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

## Key Business Questions

1. Which category generates the highest profit?
2. Which category has the strongest profit margin?
3. Which Furniture sub-categories are profitable or loss-making?
4. How are different discount levels associated with profitability for Tables?

## Key Findings

### Category Performance

Technology generated the highest total profit, followed by Office Supplies. Furniture generated substantially lower profit despite having significant sales.

### Profit Margin

Technology and Office Supplies both had profit margins of approximately 17%, while Furniture had a much lower margin of approximately 2.5%.

### Furniture Performance

Furniture performance varies significantly by sub-category.

- Furnishings had the strongest profit margin.
- Chairs were profitable.
- Bookcases had a negative profit margin.
- Tables had the weakest profit margin.

### Discount Analysis

For Tables, profitability declined sharply as discount levels increased.

The approximate profit margins were:

- 0% discount: +18%
- 20% discount: approximately 0%
- 30% discount: -13%
- 40% discount: -35%
- 45% discount: -45%
- 50% discount: -63%

This indicates a strong association between higher discounts and lower profitability for Tables.

## Business Recommendations

- Review discounting strategies for Tables, particularly at very high discount levels.
- Investigate the pricing and cost structure of Tables and Bookcases.
- Avoid applying the same discount strategy across all Furniture products.
- Protect profitable sub-categories such as Furnishings and Chairs.
- Further investigate whether product mix, costs, or order characteristics contribute to the observed losses.

## Project Structure

```text
superstore-sales-profit-analysis/
│
├── data/
│   └── Sample - Superstore.csv
│
├── visualizations/
│   └── furniture_profit_margin.png
│
├── analysis.py
└── README.md


## Conclusion

The analysis shows that strong sales do not necessarily result in strong profitability. Technology performs well in both sales and profit, while Furniture requires more targeted investigation. In particular, Tables and Bookcases show negative profitability, and higher discounts for Tables are strongly associated with increasing losses.