def Operators(day):
	if day == 1:
		def FCT(first,second):
			result = first + second
			return result
	else:
		def FCT(first,second):
			result = first - second
			return result
	return FCT

Command = Operators(int(input("Enter Function To Execute:")))
Number1 = int(input("Enter a Number:"))
Number2 = int(input("Enter Another Number:"))

print("The Result Is:", Command(Number1,Number2))