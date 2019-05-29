def Ones(InputDigit):
	if InputDigit == "1":
		return "One"
	elif InputDigit == "2":
		return "Two"
	elif InputDigit == "3":
		return "Three"
	elif InputDigit == "4":
		return "Four"
	elif InputDigit == "5":
		return "Five"
	elif InputDigit == "6":
		return "Six"
	elif InputDigit == "7":
		return "Seven"
	elif InputDigit == "8":
		return "Eight"
	elif InputDigit == "9":
		return "Nine"
	else:
		return ""

def Tens(InputDigit):
	if InputDigit == "2":
		return "Twenty"
	elif InputDigit == "3":
		return "Thirty"
	elif InputDigit == "4":
		return "Fourty"
	elif InputDigit == "5":
		return "Fifty"
	elif InputDigit == "6":
		return "Sixty"
	elif InputDigit == "7":
		return "Seventy"
	elif InputDigit == "8":
		return "Eighty"
	elif InputDigit == "9":
		return "Ninety"
	else:
		return ""

def Hundreds(InputDigit):
	if InputDigit == "0":
		return ""
	else:
		return Ones(InputDigit), "Hundred"

def Thousands(InputDigit):
	return Ones(InputDigit), "Thousand"

def Dozens(InputDigit):
	if InputDigit == "1":
		return "Eleven"
	elif InputDigit == "2":
		return "Twelve"
	elif InputDigit == "3":
		return "Thirteen"
	elif InputDigit == "4":
		return "Fourteen"
	elif InputDigit == "5":
		return "Fifteen"
	elif InputDigit == "6":
		return "Sixteen"
	elif InputDigit == "7":
		return "Seventeen"
	elif InputDigit == "8":
		return "Eighteen"
	elif InputDigit == "9":
		return "Nineteen"
	else:
		return "Ten"

def Convert(InputNum):
	NumberLen = len(str(InputNum))
	InputNum = str(InputNum)
	
	#Work out what digits to send where based on number length
	#4 Digits Long
	if NumberLen == 4:
		StringPartOne = Thousands(InputNum[0])
		StringPartTwo = Hundreds(InputNum[1])

		if InputNum[2] == "1":
			StringPartThree = Dozens(InputNum[3])
			StringPartFour = ""
		else:
			StringPartThree = Tens(InputNum[2])
			StringPartFour = Ones(InputNum[3])

	#3 Digits Long
	elif NumberLen == 3:
		StringPartOne = Hundreds(InputNum[0])

		if InputNum[1] == "1":
			StringPartTwo = Dozens(InputNum[2])
			StringPartThree = ""
		else:
			StringPartTwo = Tens(InputNum[1])
			StringPartThree = Ones(InputNum[2])

		StringPartFour = ""

	#2 Digits Long
	elif NumberLen == 2:

		if InputNum[0] == "1":
			StringPartOne = Dozens(InputNum[1])
			StringPartTwo = ""
		else:
			StringPartOne = Tens(InputNum[0])
			StringPartTwo = Ones(InputNum[1])

		StringPartThree = ""
		StringPartFour = ""

	#1 Digit Long
	else:
		#Special Case For Zero
		if InputNum[0] == "0":
			StringPartOne = "Zero"
			StringPartTwo = ""
			StringPartThree = ""
			StringPartFour = ""
		#If a single digit other than 0
		else:
			StringPartOne = Ones(InputNum[0])
			StringPartTwo = ""
			StringPartThree = ""
			StringPartFour = ""

	#Assemble the parts of the string
	FullString = StringPartOne, StringPartTwo, StringPartThree, StringPartFour
	FullString = str(FullString)

	#Fix formatting of the string by removing non-alphabetical, non-space characters
	StringLen = len(FullString)
	Counter = 0
	FixedString = ""

	while Counter < StringLen:
		if ord(FullString[Counter])>=65 and ord(FullString[Counter])<=90:
			FixedString += FullString[Counter]

		if ord(FullString[Counter])>=97 and ord(FullString[Counter])<=122:
			FixedString += FullString[Counter]

		if ord(FullString[Counter])==32:
			FixedString += FullString[Counter]

		Counter += 1

	#Return the complete string
	return FixedString
		
InputNumber = int(input("Please Enter A Number:"))
print("Your Number Is:")
print(Convert(InputNumber))