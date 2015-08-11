limit = int(2E06)

def getPrimeSum(limit):
	sum = 0
	i = 0
	toCalc = range(2, limit)
	toCalc = map(lambda x: True, toCalc)
	for j, value in enumerate(toCalc):
		if j < 2: continue
		if value:
			i += 1
			sum += j
			for k in xrange(j, limit-2, j):
				toCalc[k] = False
	return sum

print(getPrimeSum(limit))
# Solution 142913828922 in 0m0.881s