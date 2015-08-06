from math import log

def isPrime(number):
	for i in range(2, number/2+1):
		if number % i == 0:
			return False
	return True

def getPrimeAtIndex(index):
	i = 0
	estimate = int(index * log(index))
	toCalc = range(2, 2*estimate)
	toCalc = map(lambda x: True, toCalc)
	for j, value in enumerate(toCalc):
		if j < 2: continue
		if value:
			i += 1
			for k in xrange(j, 2*estimate-2, j):
				toCalc[k] = False
		if i == index:
			return j

print(getPrimeAtIndex(10001))
# Solution 104743 in 0m0.085s