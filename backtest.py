import pandas as pd
import vollib as vl
from dateutil import parse
from time import strftime
from wallstreet.blackandscholes import riskfree

class option(object):
	"""Object that caculates option greeks. Need current stock price, option's strike price, exiration month, day, and year, and sigma data to calculate implied volatility."""
	def __init__(self, underlyingPrice, strike, expry_mm, expry_dd, expry_yyyy,  sigma_data):
		super(option, self).__init__()
		self.S = underlyingPrice
		self.K = strike
		self.t = calc_t(str(expry_mm) + '-' + str(expry_dd) + '-' + str(expry_yyyy))
		self.r = calc_riskfree(self.t)
        self.sigma = calc_sigma(sigma_data)

    def calc_sigma(sigma_data):
		# return sigma
		pass

    def calc_riskfree(t):
        # get risk free rate. t is time to expiration in years.
    	rate = riskfree()
        return rate(t / float(252))

    def calc_t():
		# expry_date mm, dd, yy
        expry_date = str(mm) + '-' + str(dd) + '-' + str(yyyy)
        expry_date = p forarser.parse(expry_date)
        current_date = parser.parse(strftime('%x'))
        return expry_date - current_date


### MAIN ###

df = pd.read_csv('resources/datasets/SPY_2016.csv')

flag = 'c'
S = 201.019                   # underlying asset price
K = 170 	                  # strike price
t = float(32) / float(252)    # time to expiration in years, 252 because 252 is number of trading days in a year.
rate = riskfree()
r = get_riskfree(t) 		  # risk free interest rate
sigma = float(0.5)            # annualized standard deviation, or volatility.
