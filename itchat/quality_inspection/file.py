f = open("orders.txt")
for line in f:
	string = line.strip()
	strings = string.split(" ")
	for s in strings:
		print(s)
	print("")
f.close()