SELECT
    SUM(sales) AS total_sales,
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin,
    ROUND(AVG(discount)* 100, 2) AS avg_discount
FROM sales
