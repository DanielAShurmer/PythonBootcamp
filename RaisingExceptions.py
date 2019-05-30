Loop = True;

while Loop:
	try:
		ValueOne = int(input("Please Enter A Number:"))
		ValueTwo = int(input("Please Enter Another Number:"))
		Result = ValueOne / ValueTwo
		print(Result)
		Loop = False
	except ZeroDivisionError:
		print("You have tried to divide by zero, please try again...")
	except ValueError:
		print("You have entered a non-numerical input, please try again...")
	except:
		print("Some other error happened, please try again...")