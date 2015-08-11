collatzNumbers = {}
def collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return (3*n)+1

def sequenceLength(n):
	l = 1
	while n != 1:
		if n in collatzNumbers:
			n = collatzNumbers[n]
		else:
			collatzNumbers[n] = collatz(n)
			n = collatzNumbers[n]
		l += 1
	return l

max = 0
maxN = 0
for i in xrange(1, int(1E06)):
	result = sequenceLength(i)
	if result > max:
		max = result
		maxN = i
print(maxN)
# Solution 837799 in 0m17.057s