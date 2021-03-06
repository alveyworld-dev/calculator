def div(a, b):
	""" Return the quotient of a divided by b """
	return float(a / b)
	
#Parameters
def multiply(x, y):
	""" Return the product of x and y """
	answer = 0 # one equal sign means assignment
	if x == 0: # two equal signs means compare
		return 0
	if y == 0:
		return 0
	while y > 0:
		answer += x
		y = y - 1 
	return answer


#Tests
print "5 * 3 = ", multiply(5, 3)
print "0 * 3 = ", multiply(0, 3)
print "5 * 0 = ", multiply(5, 0)
print "-4 * 3 = ", multiply(-4, 3)
print "2.5 * 10 = ", multiply(2.5, 10)
