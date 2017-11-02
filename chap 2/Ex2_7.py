number1 = raw_input( "Enter the first number: " )
number1 = int( number1 )

number2 = raw_input( "Enter the second number: " )
number2 = int( number2 )

a = number2 % number1
if a == 0:
	print "first number is a multiple of the second"
else:
	if a != 0:
		print "first number is not a multiple of the second"
