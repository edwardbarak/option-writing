import wallstreet as ws
import yahoo_finance as yf
import math

## Variables ## op = 'option'
op = {
	'duration': {'min': 20, 'max': 40}, # measured in days
	'bwd' = {'min:': -200, 'max': 200}, # bwd = beta-weighted delta
	'd' = {'min': .08, 'max': .25}, # d = delta
}

## Functions

def find_strike_range_call(ticker=ticker):
	min_strike = {'strike': None, 'delta': None}
	max_strike = {'strike': None, 'delta': None}

	stock_price = float(yf.Share(ticker).get_price())
	stock_price_ceil = math.ceil(stock_price)
	stock = ws.Call(ticker, strike=stock_price_ceil)

	# find max strike
	for i in range(0,5):
		option = ws.Call(ticker, strike=stock_price_ceil + i)

		delta = option.delta()
		if delta <= op['d']['max']:
			max_strike = {'strike': option.strike, 'delta': delta}
			break

	# find min strike
	for i in range(0,5):
		option = ws.Call(ticker, strike=max_strike['strike'] + i)

		delta = option.delta()
		if delta <= op['d']['min']: 
			break
		else:
			min_strike = {'strike': option.strike, 'delta': delta}

	return min_strike, max_strike