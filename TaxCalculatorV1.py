Name = input("Enter Employee Name: ")
Salary = int(input("Enter Employee Salary: "))
if Salary > 20000:
	Tax = Salary * 25/100
else:
	Tax = Salary * 15/100
NetSalary = Salary - Tax
print("-----------------------------")
print("Employee ~ ", Name)
print("Salary ~ £", Salary)
print("Tax Deducted ~ £", Tax)
print("Take Home Pay ~ £", NetSalary)