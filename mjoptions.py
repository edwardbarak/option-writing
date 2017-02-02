import wallstreet as ws

## Variables ## op = 'option'
op = {
	'duration': {'min': 20, 'max': 40}, # measured in days
	'bwd': {'min:': -200, 'max': 200}, # bwd = beta-weighted delta
	'd': {'min': .08, 'max': .25}, # d = delta
}

## Functions

def strike_range_call(ticker):
	min_strike = {'strike': None, 'delta': None}
	max_strike = {'strike': None, 'delta': None}

	option = ws.Call(ticker)
	underlying_price = option.underlying.price
	
	first_strike = None
	for strike in option.strikes:
		if strike > underlying_price:
			first_strike_index = option.strikes.index(strike)
			break

	# find max strike
	for strike in option.strikes[first_strike_index:]:
		option.set_strike(strike)

		delta = option.delta()
		if delta <= op['d']['max']:
			max_strike = {'strike': option.strike, 'delta': delta}
			min_strike = {'strike': option.strike, 'delta': delta}
			max_strike_index = option.strikes.index(strike)
			break

	# find min strike
	for strike in option.strikes[max_strike_index + 1:]:
		option.set_strike(strike)

		delta = option.delta()
		if delta >= op['d']['min']:
			min_strike = {'strike': option.strike, 'delta': delta}
			break

	return {'min_strike': min_strike, 'max_strike': max_strike}