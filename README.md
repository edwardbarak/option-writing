# Option Writing
## Purpose
1. Understand MJ Demarco's option trading strategy
2. Once it is understood, attempt to backtest it
3. If proven to work in any degree, attempt to test it using fake cash and live data
4. If tests using fake cash and live data work, try with real cash and live data.
5. If real cash and live data works, attempt to automate it.

## Progress
1. (X) Purchase SPY option chain data.
2. ( ) Figure out reliable way to calculate greeks with available information.
3. ( ) Simulate MJ strategy for 20 to 40 days.

## Notes
* Reference materials can be found in references.md
* Backtest in overlapping intervals to avoid overfitting.
* possibility that wallstreet library greek calculations are not accurate (signficantly different calculated values compared to NASDAQ listed calculations)
* wallstreet library has a good function to scrape and calculate the risk free interest rate like so:
	> from wallstreet.blackandscholes import riskfree
	> rate = riskfree
	> rate(32 / float(252)) # calculates the risk free rate for a 32 day period in a full trading year. Rates are scraped and calculated via the US Treasury website.