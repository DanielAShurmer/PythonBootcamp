InputString = input("Enter a message:").upper()
CharToFind = input("Select a Character to Find:").upper()

counter = 0
CharsFound = 0

while counter < len(InputString):
	if CharToFind == InputString[counter]:
		CharsFound += 1
	counter += 1

print("Your message contains",CharsFound,"instances of the letter",CharToFind,".")