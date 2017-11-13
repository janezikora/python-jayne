

print "deg.Celsius %22s" % "temp in F"
for Celsius in range(0, 101, 10):
	
	
	A = (1.8 * (Celsius)) + 32

	print "%2d %25.1f" % (Celsius, A)

