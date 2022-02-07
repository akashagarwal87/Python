# Write your MySQL query statement below
select a.stock_name, (a.totalSell - b.totalBuy) as 'capital_gain_loss' from (select stock_name,sum(price) as 'totalSell' from stocks where operation='sell' group by stock_name) a, (select stock_name,sum(price) as 'totalBuy' from stocks where operation='buy' group by stock_name) b where a.stock_name=b.stock_name