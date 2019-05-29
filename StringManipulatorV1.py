def change(Message):
	MessageLen = len(Message)
	Counter = 0
	OutputString = ""

	while Counter < MessageLen:
		CharToEdit = ord(Message[Counter])

		if  CharToEdit>= 65 and CharToEdit <= 90:
			OutputString += chr(CharToEdit + 32)

		elif CharToEdit >= 97 and CharToEdit <= 122:
			OutputString += chr(CharToEdit - 32)

		elif CharToEdit >= 48 and CharToEdit <= 57:
			OutputString += str(int(chr(CharToEdit)) * 2)

		else:
			OutputString += chr(CharToEdit)
		Counter += 1

	return OutputString




InputString = input("Please Enter A String:")
print("The Manipulated Version Of This String Is: ", change(InputString))
