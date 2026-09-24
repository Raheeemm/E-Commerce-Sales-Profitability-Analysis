SELECT
    discount,
    COUNT(*) AS transactions,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin
FROM sales
GROUP BY discount
ORDER BY discount;