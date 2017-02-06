# Option Writing
## Purpose
1. Understand MJ Demarco's option trading strategy
2. Once it is understood, attempt to backtest it
3. If proven to work in any degree, attempt to test it using fake cash and live data
4. If tests using fake cash and live data work, try with real cash and live data.
5. If real cash and live data works, attempt to automate it.

## Progress
1. (X) Write function that finds best written call strike range for WMT for the current day according to constraints.
2. ( ) Output data to file.
3. ( ) Simulate MJ strategy for 20 to 40 days.

## Notes
* Reference materials can be found in references.md
* Need to figure out what format purchased option chain data comes in. Preferably start with SPY
* Backtest in monthly increments to avoid overfitting.
* Activate virtualenv with 'python3 -m source venv/bin/activate' in command line. 'python3 -m deactivate' to deactivate virtualenv.
