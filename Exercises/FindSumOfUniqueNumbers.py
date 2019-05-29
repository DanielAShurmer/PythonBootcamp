ListOfValues = []
CompleteList = []

FirstEntry = input("Enter Value 1:")
ListOfValues.append(FirstEntry)
CompleteList.append(FirstEntry)

ProposedEntry = input("Enter Value 2:")

if ProposedEntry in CompleteList:
	ListOfValues.remove(ProposedEntry)
else:
	ListOfValues.append(ProposedEntry)
	CompleteList.append(ProposedEntry)

ProposedEntry = input("Enter Value 3:")

if ProposedEntry in CompleteList:
	try:
		ListOfValues.remove(ProposedEntry)
	except:
		FirstEntry = 0
else:
	ListOfValues.append(ProposedEntry)
	CompleteList.append(ProposedEntry)

sumTotal = 0
for number in ListOfValues:
	sumTotal += int(number)
print(sumTotal)
