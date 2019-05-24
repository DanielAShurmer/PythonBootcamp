Num = int(input("Enter A Number: "))
if Num > 1000:
	print("B")
	if Num > 2000:
		print("C")
	else:
		print("F")
	print("2")
else:
	print("A")
	if Num > 500:
		print("E")
	else:
		print("D")
	print("1")
print("3")