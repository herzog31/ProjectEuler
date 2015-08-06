def multipleOfFive(number):
	return number % 10 == 0 or number % 10 == 5

def multipleOfThree(number):
	return quersumme(number) % 3 == 0

def quersumme(number):
	sum = 0
	while number:
		sum += number % 10
		number = int(number / 10)
	return sum

sum = 0
for i in range(1000):
	if multipleOfFive(i) or multipleOfThree(i):
		sum += i
print(sum)
# Solution 233168 in 0m0.021s