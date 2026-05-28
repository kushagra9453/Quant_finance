-- Create portfolio table
DROP TABLE IF EXISTS portfolio;
CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    buy_price REAL NOT NULL,
    current_price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    purchase_date TEXT NOT NULL,
    sector TEXT
);
-- Insert data
INSERT INTO portfolio
VALUES (
        1,
        'RELIANCE',
        2400,
        2650,
        50,
        '2024-01-15',
        'Energy'
    ),
    (2, 'INFOSYS', 1300, 1180, 30, '2024-01-20', 'IT'),
    (
        3,
        'HDFC',
        1600,
        1720,
        40,
        '2024-02-10',
        'Banking'
    ),
    (4, 'TCS', 3800, 3950, 20, '2024-02-15', 'IT'),
    (5, 'WIPRO', 520, 480, 100, '2024-03-01', 'IT'),
    (
        6,
        'HINDUNILVR',
        2300,
        2450,
        25,
        '2024-03-10',
        'FMCG'
    ),
    (
        7,
        'ICICIBANK',
        980,
        1050,
        60,
        '2024-03-15',
        'Banking'
    ),
    (
        8,
        'BHARTIARTL',
        1100,
        1255,
        45,
        '2024-03-20',
        'Telecom'
    );
SELECT *
FROM portfolio;
-- Show only symbol, buy_price, current_price for all stocks
SELECT symbol,
    buy_price,
    current_price
FROM portfolio;
-- Find all stocks where current_price > 2000
-- Show symbol, current_price, sector
SELECT symbol,
    current_price,
    sector
FROM portfolio
WHERE current_price > 2000;
-- Find all IT sector stocks
-- Show symbol, sector, buy_price
SELECT symbol,
    sector,
    buy_price
FROM portfolio
WHERE sector = "IT";
-- Calculate Profit/Loss for each stock
-- Formula: (current_price - buy_price) * quantity
-- Show symbol, sector, P&L as 'pnl'
SELECT symbol,
    sector,
    (current_price - buy_price) * quantity as pnl
FROM portfolio;
-- Find IT sector stocks with current_price > 1500
-- Show symbol, current_price, sector
SELECT symbol,
    current_price,
    sector
FROM portfolio
WHERE sector = "IT"
    AND current_price > 1500;
-- Find stocks in Energy OR Banking sector
-- Show symbol, sector
SELECT symbol,
    sector
FROM portfolio
WHERE sector = "Energy"
    OR sector = "Banking";
-- Find stocks with buy_price between 1000 and 3000
-- Show symbol, buy_price, sector
SELECT symbol,
    buy_price,
    sector
FROM portfolio
WHERE buy_price BETWEEN 1000 AND 3000;
-- Find stocks in 'IT' or 'Banking' sector using IN
-- Show symbol, sector
SELECT symbol,
    sector
FROM portfolio
WHERE sector in ("IT", "Banking");
-- Find all stocks NOT in IT sector
-- Show symbol, sector
SELECT symbol,
    sector
FROM portfolio
WHERE sector NOT IN ("IT");
-- Find stocks starting with 'H' using LIKE
-- Show symbol
SELECT symbol
FROM portfolio
WHERE symbol LIKE "H%";
-- Find stocks where sector is NOT NULL
-- Show symbol, sector
SELECT symbol,
    sector
FROM portfolio
WHERE sector IS NOT NULL;
-- Create profit_status column:
-- 'PROFIT' if current_price > buy_price
-- 'LOSS' if current_price < buy_price
-- 'BREAK EVEN' if equal
-- Show symbol, buy_price, current_price, profit_status
SELECT symbol,
    buy_price,
    current_price,
    CASE
        WHEN current_price > buy_price THEN "profit"
        WHEN current_price < buy_price THEN "loss"
        ELSE "break even"
    END profit_status
FROM portfolio;
-- Show for each stock:
-- symbol, quantity, buy_price, current_price
-- total_invested = buy_price * quantity
-- total_current = current_price * quantity
-- pnl = total_current - total_invested
-- pnl_percent rounded to 2 decimals
SELECT symbol,
    quantity,
    buy_price,
    current_price,
    buy_price * quantity AS total_invested,
    current_price * quantity AS total_current,
    (current_price * quantity) - (buy_price * quantity) AS pnl,
    ROUND(
        (
            (current_price * quantity) - (buy_price * quantity)
        ) * 100.0 / (buy_price * quantity),
        2
    ) AS pnl_percent
FROM portfolio;
-- Find stocks with buy_price greater than average buy_price
-- Show symbol, buy_price, and the average buy_price
SELECT symbol,
    buy_price,
    (
        SELECT AVG(buy_price)
        FROM portfolio
    ) AS avg_buy_price
FROM portfolio
WHERE buy_price >(
        SELECT AVG(buy_price)
        FROM portfolio
    );
-- Find profitable stocks (current > buy)
-- in IT or Banking sector
-- with quantity >= 30
-- Sort by P&L highest first
SELECT symbol,
    buy_price,
    current_price,
    sector,
    quantity,
    (current_price - buy_price) * quantity AS pnl
FROM portfolio
WHERE current_price > buy_price
    AND quantity >= 30
    AND sector IN ("IT", "Banking")
ORDER BY pnl DESC;
-- Create table 'profitable_stocks'
-- Insert all profitable stocks with symbol, buy_price, current_price, pnl
CREATE TABLE IF NOT EXISTS profitable_stocks (
    symbol TEXT,
    buy_price REAL,
    current_price REAL,
    pnl REAL
);
INSERT INTO profitable_stocks(symbol, buy_price, current_price, pnl)
SELECT symbol,
    buy_price,
    current_price,
    (current_price - buy_price) * quantity
FROM portfolio
WHERE current_price > buy_price;
SELECT *
FROM profitable_stocks;
-- Write a query that returns:
-- total_invested, total_current, total_pnl, total_return_percent
-- profitable_stocks_count, loss_stocks_count
-- best_performing_stock, worst_performing_stock
SELECT SUM(buy_price * quantity) AS total_invested,
    SUM(current_price * quantity) AS total_current,
    SUM((current_price - buy_price) * quantity) AS total_pnl,
    ROUND(
        SUM((current_price - buy_price) * quantity) * 100.0 / SUM(buy_price * quantity),
        2
    ) AS total_return_percent,
    SUM(
        CASE
            WHEN current_price > buy_price THEN 1
            ELSE 0
        END
    ) AS profitable_stocks,
    SUM(
        CASE
            WHEN current_price < buy_price THEN 1
            ELSE 0
        END
    ) AS loss_stocks,
    (
        SELECT symbol
        FROM portfolio
        ORDER BY (current_price - buy_price) * quantity DESC
        LIMIT 1
    ) AS best_stock,
    (
        SELECT symbol
        FROM portfolio
        ORDER BY (current_price - buy_price) * quantity ASC
        LIMIT 1
    ) AS worst_stock
FROM portfolio;