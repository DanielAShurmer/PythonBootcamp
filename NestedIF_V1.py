Num = int(input("Enter a Number: "))
if Num > 1000:
	print("Number is over 1000.")
	if Num > 2000:
		print("Number is also over 2000.")
else:
	print("Number is equal to or under 1000.")
	if Num < 500:
		print("Number is also under 500.")