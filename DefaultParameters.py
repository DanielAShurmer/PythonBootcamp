def Tax(Salary,TaxRate = 21):
	IncomeTax = Salary * (TaxRate / 100)
	print("Your Salary Is:",Salary - IncomeTax)

Tax(15000)
Tax(23000)
Tax(12500,15)