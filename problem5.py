from sets import Set

def isPrime(number):
	for i in range(2, number/2+1):
		if number % i == 0:
			return False
	return True

divisors = range(1,21)
maximum = reduce(lambda x,y: x*y, range(1, 21))
minimum = 1
for i in divisors:
	if isPrime(i):
		minimum = minimum * i

for i in xrange(minimum, maximum, +minimum):
	print(i)
	for j in divisors:
		if i % j != 0:
			break
	else:
		print (i)
		break
# Solution 232792560 in 0m0.023s