prev = 1
cur = sum = 2
while cur < 4E06:
	new = cur + prev
	prev = cur
	cur = new
	if cur % 2 == 0:
		sum += new
print(sum)
# Solution 4613732 in 0m0.023s