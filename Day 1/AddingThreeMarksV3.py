Physics = input("Enter Physics Mark:")
Chemistry = input("Enter Chemistry Mark:")
Maths = input("Enter Maths Mark:")
Total = int(Physics) + int(Chemistry) + int(Maths)
Percent = Total * 100/150
print("---------------------------")
print("Total Marks: ", Total)
print("Percentage: ", Percent, "%")
print("---------------------------")