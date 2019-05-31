Command = int(input("Enter Function To Execute:"))
Number1 = int(input("Enter a Number:"))
Number2 = int(input("Enter Another Number:"))

if Command == 1:
	def FCT(first,second):
		result = first + second
		return result
else:
	def FCT(first,second):
		result = first - second
		return result

print("The Result Is:", FCT(Number1,Number2))