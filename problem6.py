from math import pow

sumSquare = int(pow(reduce(lambda x,y: x+y, range(1,101)), 2))
squareSum = map(lambda x: pow(x,2), range(1,101))
squareSum = int(reduce(lambda x,y: x+y, squareSum))
result = abs(squareSum - sumSquare)
print(result)
# Solution 25164150 in 0m0.021s