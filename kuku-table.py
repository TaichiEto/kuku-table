for i in range(1, 10):
	print("{}の段".format(i))
	for j in range(1, 10):
		print("{} * {} = ".format(i,j) + str(i * j), end=" ")
		print("")
	print("")