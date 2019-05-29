Value = int(input("Enter a Starting Value:"))
EndValue = int(input("Enter an Ending Value:"))
while Value <= EndValue:
	if Value % 2 == 0:
		print(Value, "is even.")
	else:
		print(Value, "is odd.")
	Value += 1
