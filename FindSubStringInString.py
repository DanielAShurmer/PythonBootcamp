InputString = input("Please enter a Message:")
Substring = input("Please enter a Substring to Search:")

counter = 0
NumberOfMatches = 0
SubStrLen = len(Substring)

while counter < len(InputString):
	if InputString[counter:counter+SubStrLen] == Substring:
		NumberOfMatches += 1
	counter += 1

print("This substring appears", NumberOfMatches , "times.")