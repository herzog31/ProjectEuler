def isPalindrom(number):
	sNumber = str(number)
	for i in xrange(len(sNumber)/2):
		if sNumber[i] != sNumber[len(sNumber)-(i+1)]:
			return False
	return True

max = 0
for i in reversed(xrange(999)):
	for j in reversed(xrange(i)):
		if isPalindrom(i*j) and (i*j) > max:
			max = (i*j)
print(max)
# Solution 906609 in 0m0.385s