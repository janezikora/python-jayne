

def factorial(number):
	fact=1
	for x in range(1,number+1):
		fact = fact*x
	return fact



number = int(raw_input("Enter a non negative integer: "))
if (number == 1) |(number == 0):
	print "The factorial is 1"
else:
	while number < 0:
		print "factorial of negative integers do not exist"
		number = int(raw_input("Enter a non negative integer: "))
	   
	fact = factorial(number)
	print "Factorial of", number, "is", fact



