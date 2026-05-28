DROP TABLE IF EXISTS portfolio;
DROP TABLE IF EXISTS daily_prices;
CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    sector TEXT,
    buy_price REAL,
    current_price REAL,
    quantity INTEGER,
    purchase_date TEXT
);

CREATE TABLE daily_prices (
    price_id INTEGER PRIMARY KEY,
    symbol TEXT,
    price_date TEXT,
    close_price REAL
);

INSERT INTO portfolio VALUES 
(1, 'RELIANCE', 'Energy', 2400, 2650, 50, '2024-01-15'),
(2, 'INFOSYS', 'IT', 1300, 1180, 30, '2024-01-20'),
(3, 'HDFC', 'Banking', 1600, 1720, 40, '2024-02-10'),
(4, 'TCS', 'IT', 3800, 3950, 20, '2024-02-15'),
(5, 'ICICIBANK', 'Banking', 980, 1050, 60, '2024-03-15');

INSERT INTO daily_prices VALUES 
(1, 'RELIANCE', '2024-05-27', 2650),
(2, 'INFOSYS', '2024-05-27', 1180),
(3, 'HDFC', '2024-05-27', 1720),
(4, 'TCS', '2024-05-27', 3950),
(5, 'ICICIBANK', '2024-05-27', 1050);

-- ========== QUESTIONS ==========

-- Q1: Complete portfolio summary (invested, current, P&L, return %)
SELECT 
    'TOTAL' as metric,
    SUM(buy_price * quantity) as total_invested,
    SUM(current_price * quantity) as total_current,
    SUM((current_price - buy_price) * quantity) as total_pnl,
    ROUND(100.0 * SUM((current_price - buy_price) * quantity) / SUM(buy_price * quantity), 2) as return_pct
FROM portfolio;

-- Q2: Sector-wise performance summary
SELECT 
    sector,
    SUM(buy_price * quantity) as total_invested,
    SUM(current_price * quantity) as total_current,
    SUM((current_price - buy_price) * quantity) as total_pnl,
    ROUND(100.0 * SUM((current_price - buy_price) * quantity) / SUM(buy_price * quantity), 2) as return_pct
FROM portfolio
GROUP BY sector;

-- Q3: Find best and worst performing stock
SELECT * FROM (
    SELECT symbol, ROUND(100.0 * (current_price - buy_price) / buy_price, 2) as return_pct, 'Best' as performance_type 
    FROM portfolio 
    ORDER BY return_pct DESC 
    LIMIT 1
) 
UNION ALL 
SELECT * FROM (
    SELECT symbol, ROUND(100.0 * (current_price - buy_price) / buy_price, 2) as return_pct, 'Worst' as performance_type 
    FROM portfolio 
    ORDER BY return_pct ASC 
    LIMIT 1
);

-- Q4: Calculate portfolio concentration (top 2 holdings %)
SELECT 
    ROUND(100.0 * SUM(current_value) / (SELECT SUM(current_price * quantity) FROM portfolio), 2) as top_2_concentration_pct
FROM (
    SELECT current_price * quantity as current_value
    FROM portfolio
    ORDER BY current_value DESC
    LIMIT 2
);

-- Q5: Show stocks purchased in each month
SELECT 
    strftime('%Y-%m', purchase_date) as purchase_month,
    GROUP_CONCAT(symbol, ', ') as stocks
FROM portfolio
GROUP BY purchase_month
ORDER BY purchase_month;

-- Q6: Calculate weighted average return of portfolio
SELECT 
    ROUND(SUM(((current_price - buy_price) / buy_price) * (buy_price * quantity)) * 100.0 / SUM(buy_price * quantity), 2) as weighted_avg_return_pct
FROM portfolio;

-- Q7: Find stocks that are underperforming (return < 0)
SELECT 
    symbol,
    buy_price,
    current_price,
    ROUND(100.0 * (current_price - buy_price) / buy_price, 2) as return_pct
FROM portfolio
WHERE current_price < buy_price;

-- Q8: Generate executive report with all metrics
SELECT 
    SUM(buy_price * quantity) as total_invested,
    SUM(current_price * quantity) as total_current,
    SUM((current_price - buy_price) * quantity) as total_pnl,
    ROUND(100.0 * SUM((current_price - buy_price) * quantity) / SUM(buy_price * quantity), 2) as return_pct,
    COUNT(CASE WHEN current_price > buy_price THEN 1 END) as profitable_count,
    COUNT(CASE WHEN current_price < buy_price THEN 1 END) as loss_count,
    (SELECT symbol FROM portfolio ORDER BY (current_price - buy_price) / buy_price DESC LIMIT 1) as best_stock,
    (SELECT symbol FROM portfolio ORDER BY (current_price - buy_price) / buy_price ASC LIMIT 1) as worst_stock
FROM portfolio;

-- Q9: Calculate daily portfolio value (JOIN with daily_prices)
SELECT 
    dp.price_date,
    SUM(dp.close_price * p.quantity) as daily_portfolio_value
FROM portfolio p
INNER JOIN daily_prices dp ON p.symbol = dp.symbol
GROUP BY dp.price_date
ORDER BY dp.price_date;

-- Q10: Show profit distribution by sector
SELECT 
    sector,
    SUM((current_price - buy_price) * quantity) as sector_pnl,
    ROUND(100.0 * SUM((current_price - buy_price) * quantity) / (SELECT SUM((current_price - buy_price) * quantity) FROM portfolio), 2) as profit_share_pct
FROM portfolio
GROUP BY sector
ORDER BY profit_share_pct DESC;

