from math import log

def isPrime(number):
	for i in range(2, number/2+1):
		if number % i == 0:
			return False
	return True

def getPrimeAtIndex(index):
	i = 0
	estimate = int(index * log(index))
	for j in xrange(2, 2*estimate):
		if isPrime(j):
			i += 1
		if i == index:
			return j

print(getPrimeAtIndex(10001))
# Solution 104743 in 0m34.966s