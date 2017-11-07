print "Enter five digit interger: "
a = raw_input("Enter the first digit: ")
b = raw_input("Enter the second digit: ")
c = raw_input("Enter the third digit: ")
d = raw_input("Enter the fourth digit: ")
e = raw_input("Enter the fifth digit: ")
A = a + b + c + d + e
print A
if (a == e) & (b == d):
	print "the five digit integer is a palindrome"
else:
	print "the five digit integer is not a palindrome"
