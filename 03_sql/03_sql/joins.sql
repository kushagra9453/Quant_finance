DROP TABLE IF EXISTS portfolio;
DROP TABLE IF EXISTS trades;
DROP TABLE IF EXISTS sectors;


CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    buy_price REAL,
    current_price REAL,
    quantity INTEGER
);

CREATE TABLE trades (
    trade_id INTEGER PRIMARY KEY,
    symbol TEXT,
    trade_type TEXT,
    price REAL,
    quantity INTEGER,
    trade_date TEXT
);

CREATE TABLE sectors (
    symbol TEXT,
    sector TEXT
);

INSERT INTO portfolio VALUES 
(1, 'RELIANCE', 2400, 2650, 50),
(2, 'INFOSYS', 1300, 1180, 30),
(3, 'HDFC', 1600, 1720, 40),
(4, 'TCS', 3800, 3950, 20);

INSERT INTO trades VALUES 
(1, 'RELIANCE', 'BUY', 2400, 50, '2024-01-15'),
(2, 'INFOSYS', 'BUY', 1300, 30, '2024-01-20'),
(3, 'HDFC', 'BUY', 1600, 40, '2024-02-10'),
(4, 'RELIANCE', 'SELL', 2650, 30, '2024-04-20'),
(5, 'WIPRO', 'BUY', 500, 100, '2024-03-01');

INSERT INTO sectors VALUES 
('RELIANCE', 'Energy'),
('INFOSYS', 'IT'),
('HDFC', 'Banking'),
('TCS', 'IT'),
('WIPRO', 'IT');



-- A1: INNER JOIN - only stocks that have trades
SELECT p.symbol, p.buy_price, t.trade_type, t.price
FROM portfolio p
INNER JOIN trades t ON p.symbol = t.symbol;

-- A2: LEFT JOIN - all stocks, even without trades
SELECT p.symbol, p.buy_price, t.trade_type, t.price
FROM portfolio p
LEFT JOIN trades t ON p.symbol = t.symbol;

-- A3: RIGHT JOIN - all trades, even if stock not in portfolio
SELECT p.symbol, t.trade_type, t.price
FROM portfolio p
RIGHT JOIN trades t ON p.symbol = t.symbol;

-- A4: JOIN with sectors table
SELECT p.symbol, p.buy_price, s.sector
FROM portfolio p
INNER JOIN sectors s ON p.symbol = s.symbol;

-- A5: P&L for sell trades
SELECT p.symbol, 
       t.price as sell_price,
       p.buy_price,
       t.quantity,
       (t.price - p.buy_price) * t.quantity as trade_pnl
FROM portfolio p
INNER JOIN trades t ON p.symbol = t.symbol
WHERE t.trade_type = 'SELL';

-- A6: Stocks never traded
SELECT p.symbol, p.buy_price
FROM portfolio p
LEFT JOIN trades t ON p.symbol = t.symbol
WHERE t.trade_id IS NULL;

-- A7: Join 3 tables (portfolio, trades, sectors)
SELECT p.symbol, s.sector, t.trade_type, t.price, t.quantity
FROM portfolio p
INNER JOIN trades t ON p.symbol = t.symbol
INNER JOIN sectors s ON p.symbol = s.symbol;

-- A8: Total quantity traded per stock
SELECT p.symbol, SUM(t.quantity) as total_traded
FROM portfolio p
INNER JOIN trades t ON p.symbol = t.symbol
GROUP BY p.symbol;

-- A9: Trades after specific date
SELECT p.symbol, t.trade_type, t.price, t.trade_date
FROM portfolio p
INNER JOIN trades t ON p.symbol = t.symbol
WHERE t.trade_date > '2024-02-01';

-- A10: Self JOIN - stocks with same buy_price
SELECT a.symbol as stock1, b.symbol as stock2, a.buy_price
FROM portfolio a
INNER JOIN portfolio b ON a.buy_price = b.buy_price AND a.symbol < b.symbol;
