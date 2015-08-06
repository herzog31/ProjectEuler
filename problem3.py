def isPrime(number):
	for i in range(2, number/2+1):
		if number % i == 0:
			return False
	return True

number = 600851475143
for i in xrange(2, number/2+1):
	if isPrime(i) and number % i == 0:
		number = number / i
		if number == 1:
			break
print(i)
# Solution 6857 in 0m0.184