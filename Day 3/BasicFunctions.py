def MSG():
	print("This")
	print("is a")
	print("message.")

def Addition(A,B):
	result = A + B
	print("The Result Is:",result)

def Tax(Salary):
	if Salary >= 1500:
		T = Salary * 21/100
	else:
		T = Salary * 15/100
	return T

MSG()

Addition(3,5)
Addition(8,4)

SalOne = int(input("Please enter your salary:"))
TaxedSal = Tax(SalOne)
print("Your Tax:",TaxedSal)
print("Your Net Salary:",SalOne-TaxedSal)

