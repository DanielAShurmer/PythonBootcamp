InputChar = input("Please enter a character:")

InputASCII = ord(InputChar)

if InputASCII >= 65 and InputASCII <= 90:
	print(chr(InputASCII + 32))

elif InputASCII >= 97 and InputASCII <= 122:
	print(chr(InputASCII - 32))

else:
	print("The character you entered is invalid.")