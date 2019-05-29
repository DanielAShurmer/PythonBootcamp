InputString = input("Enter a Message:")
Word = ""
Counter = 0

while Counter < len(InputString):
	if InputString[Counter] ==  " ":
		print(Word)
		Word = ""
	else:
		Word += InputString[Counter]
	Counter += 1

print(Word)