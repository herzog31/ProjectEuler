def getNumberOfDevisors(number):
	if number == 1:
		return 1
	i = n = 2
	limit = number
	while i < limit:
		if number % i == 0:
			n += 2
			limit = number / i
		i += 1
	return n

d = 0
n = 1
sum = 0
while d <= 500:
	sum += n
	n += 1
	d = getNumberOfDevisors(sum)

print(sum)
# Solution 76576500 in 0m6.066s