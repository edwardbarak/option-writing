import pandas as pd
import vollib as vl
import dateutil
from datetime import timedelta

# dateutil.parser.parse('2016-01-01') 
# dateutil.timedelta(end_date, start_date).days / float(365)
#vl.b

df = pd.read_csv('resources/datasets/SPY_2016.csv')

flag = 'c'
S = 201.019 # underlying asset price
K = 170 	# strike price
t = float(32) / float(252) # time to expiration in years, 252 because 252 is number of trading days in a year.
r = float(.51) 		#risk free interest rate
sigma = float(0.5) # annualized standard deviation, or volatility.
 
class option(object):
	"""docstring for option"""
	def __init__(self, underlyingPrice, strike, start_date, end_date, risk_free_rate, sigma_data):
		super(option, self).__init__()
		self.S = underlyingPrice
		self.K = strike
		self.start_date = start_date
		self.end_date = end_date
		self.r = risk_free_rate
	def calc_sigma():
		# calculate sigma via sigma_data df
		# self.sigma = sigma
		pass
	def calc_t():
		self.end_date = dateutil.parser.parse(self.end_date)
		self.start_date = dateutil.parser.parse(self.start_date)
		option_days = timedelta(end_date, start_date)
		self.t = option_days / float(252)
	def calc_greeks():
		pass

def get_r():
	# get risk free rate
	pass	