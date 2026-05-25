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