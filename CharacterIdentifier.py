InputChar = input("Please enter a character:")

InputASCII = ord(InputChar)

if InputASCII >= 65 and InputASCII <= 90:
	print("Uppercase")

elif InputASCII >= 97 and InputASCII <= 122:
	print("Lowercase")

elif InputASCII >= 48 and InputASCII <= 57:
	print("Numerical")

else:
	print("Special")