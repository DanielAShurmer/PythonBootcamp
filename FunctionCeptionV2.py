def Addition(A,B):
	Result = A + B
	return Result

def Subtraction(A,B):
	Result = A - B
	return Result

def Operation(Funct,A,B):
	if Funct == 1:
		Result = Addition(A,B)
	else:
		Result = Subtraction(A,B)
	return Result

Command = int(input("Enter Function To Execute:"))
Number1 = int(input("Enter a Number:"))
Number2 = int(input("Enter Another Number:"))


print("The Result Is:" + str(Operation(Command,Number1,Number2)))