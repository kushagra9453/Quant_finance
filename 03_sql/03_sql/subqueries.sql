-- Delete old table if already exists
DROP TABLE IF EXISTS portfolio;
-- Create table
CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    buy_price REAL,
    current_price REAL,
    quantity INTEGER,
    sector TEXT
);
-- Insert data
INSERT INTO portfolio
VALUES (1, 'RELIANCE', 2400, 2650, 50, 'Energy'),
    (2, 'INFOSYS', 1300, 1180, 30, 'IT'),
    (3, 'HDFC', 1600, 1720, 40, 'Banking'),
    (4, 'TCS', 3800, 3950, 20, 'IT'),
    (5, 'ICICIBANK', 980, 1050, 60, 'Banking');
-- Check data
-- A1: Above average current price
SELECT symbol,
    current_price
FROM portfolio
WHERE current_price > (
        SELECT AVG(current_price)
        FROM portfolio
    );
-- A2: Above average buy price
SELECT symbol,
    buy_price
FROM portfolio
WHERE buy_price > (
        SELECT AVG(buy_price)
        FROM portfolio
    );
-- A3: Second highest current price
SELECT MAX(current_price) as second_highest
FROM portfolio
WHERE current_price < (
        SELECT MAX(current_price)
        FROM portfolio
    );
-- A4: P&L greater than average P&L
SELECT symbol,
    (current_price - buy_price) * quantity as pnl
FROM portfolio
WHERE (current_price - buy_price) * quantity > (
        SELECT AVG((current_price - buy_price) * quantity)
        FROM portfolio
    );
-- A5: Sectors with above average return
SELECT DISTINCT sector
FROM portfolio p1
WHERE ((current_price - buy_price) * 100.0 / buy_price) > (
        SELECT AVG((current_price - buy_price) * 100.0 / buy_price)
        FROM portfolio p2
        WHERE p2.sector = p1.sector
    );
-- A6: Profitable stocks using IN
SELECT symbol,
    current_price,
    buy_price
FROM portfolio
WHERE symbol IN (
        SELECT symbol
        FROM portfolio
        WHERE current_price > buy_price
    );
-- A7: Above average quantity
SELECT symbol,
    quantity
FROM portfolio
WHERE quantity > (
        SELECT AVG(quantity)
        FROM portfolio
    );
-- A8: Sectors with above average total P&L
SELECT sector,
    SUM((current_price - buy_price) * quantity) as sector_pnl
FROM portfolio
GROUP BY sector
HAVING sector_pnl > (
        SELECT AVG(total_pnl)
        FROM (
                SELECT SUM((current_price - buy_price) * quantity) as total_pnl
                FROM portfolio
                GROUP BY sector
            )
    );
-- A9: Stocks that outperformed sector average
SELECT p1.symbol,
    p1.sector,
    (
        (p1.current_price - p1.buy_price) * 100.0 / p1.buy_price
    ) as stock_return,
    (
        SELECT AVG(
                (p2.current_price - p2.buy_price) * 100.0 / p2.buy_price
            )
        FROM portfolio p2
        WHERE p2.sector = p1.sector
    ) as sector_avg_return
FROM portfolio p1
WHERE (
        (p1.current_price - p1.buy_price) * 100.0 / p1.buy_price
    ) > (
        SELECT AVG(
                (p2.current_price - p2.buy_price) * 100.0 / p2.buy_price
            )
        FROM portfolio p2
        WHERE p2.sector = p1.sector
    );
-- A10: Highest P&L in each sector (correlated subquery)
SELECT p1.symbol,
    p1.sector,
    (p1.current_price - p1.buy_price) * p1.quantity as pnl
FROM portfolio p1
WHERE (p1.current_price - p1.buy_price) * p1.quantity = (
        SELECT MAX((p2.current_price - p2.buy_price) * p2.quantity)
        FROM portfolio p2
        WHERE p2.sector = p1.sector
    );