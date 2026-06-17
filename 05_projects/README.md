# Portfolio Optimization (Mean-Variance)

## Project Overview
This project implements the classic **Markowitz Mean-Variance Optimization** to find the optimal asset allocation for a portfolio of Indian stocks. It calculates the **Efficient Frontier** and identifies the portfolio that maximizes the **Sharpe ratio**.

## Data & Methodology
- **Stocks used:** RELIANCE.NS, TCS.NS, HDFCBANK.NS, INFY.NS, ICICIBANK.NS
- **Data source:** `yfinance` (daily closing prices from 2023-01-01 to 2024-12-31)
- **Risk-free rate:** Assumed 5% (annual)
- **Approach:**  
  - Annualized returns and covariance matrix from daily returns.
  - Random portfolio simulation (10,000 portfolios) to visualise the Efficient Frontier.
  - Maximum Sharpe ratio portfolio identified from random samples.

## Key Results
- **Optimal weights (max Sharpe):**  
  [e.g., RELIANCE: 0.15, TCS: 0.30, HDFCBANK: 0.20, INFY: 0.25, ICICIBANK: 0.10]
- **Expected annual return of optimal portfolio:** XX.XX%
- **Annual volatility of optimal portfolio:** XX.XX%
- **Sharpe ratio:** X.XX

## Visualisations
- **Efficient Frontier:** Scatter plot of risk (std dev) vs return, coloured by Sharpe ratio.
- (Optional) Capital Market Line

## Libraries Used
- `yfinance` – data download
- `pandas` – data manipulation
- `numpy` – mathematical operations
- `matplotlib` – plotting
- `scipy.optimize` (optional) – exact optimisation

## How to Run
1. Install required libraries:  
   `pip install yfinance pandas numpy matplotlib scipy`
2. Run the Jupyter notebook `portfolio_optimization.ipynb` or the Python script.
3. The output will display optimal weights, metrics, and plots.

## Future Improvements
- Add constraints (e.g., no short selling, sector limits).
- Use daily return forecasts instead of historical averages.
- Implement Black‑Litterman or other advanced models.

## References
- Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*.
- Hull, J. (2022). *Options, Futures, and Other Derivatives* (Chapter 1).
