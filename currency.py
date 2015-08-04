# Currency Exchange Arbitrage Simulation
# Returns the best arbitrage opportunity in a random set of exchange rates
# Usage: python currency.py <number of currencies> <length of chain>
# Stephen Ellis

import random
import math
import sys
import itertools

def new_rate(range):
	tail = range / 2
	res = random.uniform(1-tail,1+tail) # generated exchange rates are in [1-range/2,1+range/2)
	return res

def profit(chain,exch): 
	'''returns profit of arbitrage chain given exchange rates'''
	trades = [(chain[i],chain[i+1]) for i in range(len(chain)) if i < len(chain) - 1]
	trades.append((chain[-1],chain[0])) #add the trade to get back to original currency
	value = 1.00
	for t in trades:
		value *= exch[t]
	return value

def get_rates(n):
	'''fill exhange rates with random numbers'''
	exch = {}
	for i in range(n):
		for j in range(i+1,n):
			rate = new_rate(.5)
			exch[(i,j)] = rate
	temp = {}
	for x,y in exch:
		temp[(y,x)] = float(1/exch[(x,y)])
	result = exch.copy()
	result.update(temp)
	return result

if __name__ == '__main__':
	N = int(sys.argv[1]) # the number of currencies
	C = int(sys.argv[2]) # the length of the chain
	exch = get_rates(N) # generate all exchange rates
	chains = list(itertools.permutations(range(N),C)) # generate all possbile chains
	results = {}
	for chain in chains:
		results[chain] = profit(chain,exch)

	''' print each exchange rate '''
	#print 'Exchange rates:'
	#for rate in exch:
		#print str(rate)+': '+str(exch[rate])
	''' '''

	max_chain = max(results.iterkeys(), key=(lambda key: results[key]))
	print 'Most profitable chain of size '+str(C)+' is ',max_chain
	print 'Ratio: '+str(results[max_chain])