from math import pow

def tripletSum(sum):
	for u in xrange(2,101):
		for v in xrange(2,101):
			if u < v: continue
			a = int(pow(u, 2) - pow(v, 2))
			b = 2 * u * v
			c = int(pow(u, 2) + pow(v, 2))
			if a + b + c == sum:
				return [a, b, c]
triplet = tripletSum(1000)
print(reduce(lambda x,y: x*y, triplet))
# Solution 31875000 in 0m0.022s