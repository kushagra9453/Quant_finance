DROP TABLE IF EXISTS portfolio;

CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    sector TEXT,
    buy_price REAL,
    current_price REAL,
    quantity INTEGER,
    purchase_date TEXT
);

INSERT INTO portfolio
VALUES (
        1,
        'RELIANCE',
        'Energy',
        2400,
        2650,
        5,
        '2003-01-23'
    ),
    (2, 'INFOSYS', 'IT', 1300, 1180, 30, '2006-01-23'),
    (3, 'HDFC', 'Banking', 1600, 1720, 40, '2003-09-23'),
    (4, 'TCS', 'IT', 3800, 3950, 20, '2003-01-13'),
    (
        5,
        'ICICIBANK',
        'Banking',
        980,
        1050,
        60,
        '2007-01-23'
    ),
    (
        6,
        'HINDUNILVR',
        'FMCG',
        2300,
        2450,
        25,
        '2003-05-23'
    );

---count number of stocks in each sector
SELECT sector,
    COUNT(*) stocks
FROM portfolio
GROUP BY sector;



-- Q2: Calculate total P&L for each sector
SELECT sector,
  SUM((current_price - buy_price) * quantity) as total_pnl
FROM portfolio
GROUP BY sector;

-- Q3: Calculate average return percentage by sector
SELECT sector,
AVG(((current_price - buy_price) * 100.0) / buy_price) as avg_return
FROM portfolio
GROUP BY sector;


-- Formula: ((current_price - buy_price) / buy_price) * 100

-- Q4: Find sectors with total P&L greater than 5000
SELECT sector,
SUM((current_price - buy_price) * quantity) as total_pnl
FROM portfolio
GROUP BY sector
HAVING total_pnl > 5000;


-- Q5: Find sectors with more than 1 stock
SELECT sector, COUNT(*) as stocks_count
FROM portfolio
GROUP BY sector
HAVING COUNT(*)> 1;
-- Q6: Find sectors where average return > 5%
SELECT sector,
  AVG(((current_price - buy_price) * 100.0) / buy_price) as avg_return_pct
FROM portfolio
GROUP BY sector
HAVING avg_return_pct > 5;


-- Q7: For each sector, show min and max buy price
SELECT sector,
MAX (buy_price) as max_buy_price,
MIN (buy_price) as min_buy_price
FROM portfolio
GROUP BY sector;
-- Q8: Group by sector and profitability status (PROFIT/LOSS)
SELECT sector,
    CASE 
        WHEN current_price > buy_price THEN 'PROFIT'
        ELSE 'LOSS'
    END AS profitability_status,
    COUNT(*) as stock_count
FROM portfolio
GROUP BY sector,
    CASE 
        WHEN current_price > buy_price THEN 'PROFIT'
        ELSE 'LOSS'
    END;