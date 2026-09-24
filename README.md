# E-Commerce Sales Analysis

## Project Overview

An end-to-end data analytics project analyzing e-commerce sales,
profitability, regional performance, customer segments, product
categories, and discount patterns.

## Business Objective

The objective was to understand sales and profitability performance
and identify areas requiring further business investigation.

## Tools Used

- Python
- Pandas
- Excel
- MySQL
- Power BI

## Analytics Workflow

Raw Data
→ Data Profiling
→ Data Cleaning
→ Exploratory Data Analysis
→ Excel Analysis
→ SQL Analysis
→ Power BI Dashboard
→ Business Insights

## Dataset

The project uses a Superstore-style transactional dataset containing
sales, profit, quantity, discount, category, sub-category, region,
and customer segment information.

## Key Analysis

- Overall sales and profitability
- Category performance
- Regional performance
- Customer segment analysis
- Sub-category profitability
- Discount and profitability analysis

## Key Findings

## 1. Regional Profitability
West generated the highest total profit at approximately $108.4K,
while Central generated the lowest at approximately $39.7K.

## 2. Category Performance
Technology generated the highest sales and profit among the three
categories, with approximately $836.2K in sales and $145.5K in profit.

## 3. Furniture Profitability
Furniture generated approximately $742K in sales but only $18.5K
in profit, indicating substantially lower profitability than
Technology and Office Supplies.

## 4. Discount and Profitability
Transactions with discounts above 20% were associated with negative
aggregate profitability in the dataset. Higher discount levels
showed particularly large losses.

## 5. Customer Segment
Consumer generated the highest sales and profit among the three
customer segments, with approximately $1.16M in sales and $134.1K
in profit.

## 6. Sub-Category Losses
Tables generated the largest sub-category loss at approximately
-$17.7K despite generating around $207K in sales

## Dashboard

![alt text](image.png)

## Project Structure

ecommerce-sales-analysis/
│
├── data/
│   ├── raw/
│   │   └── SampleSuperstore.csv
│   │
│   └── cleaned/
│       └── superstore_clean.csv
│
├── python/ 
│   ├── 01_data_cleaning.py
│   └── 02_eda.py
│
├── sql/
│   ├── business_analysis.sql
│   ├── category_analysis.sql
│   ├── discount_analysis.sql
│   ├── kpi_analysis.sql
│   ├── regional_analysis.sql
│   ├── segment_analysis.sql
│   └── sub_category_analysis.sql
│
├── excel/
│   └── ecommerce_analysis.xlsx
│
├── powerbi/
│   └── Ecommerce_analysis.pbix
│
├── analysis/
│   └── findings.md
│
├── screenshots/
│   └── dashboard.png
│
├── README.md
│
└── .gitignore

## Conclusion

The analysis identified significant differences in profitability
across regions, categories, and discount levels. The findings can
help identify areas for further investigation around pricing,
discounting, product mix, and regional performance.