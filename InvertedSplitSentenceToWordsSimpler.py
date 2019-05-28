InputString = " " + input("Enter a Message:")
Word = ""
Counter = len(InputString) - 1

while Counter >= 0:
	if InputString[Counter] ==  " ":
		print(Word)
		Word = ""
	else:
		Word = InputString[Counter] + Word
	Counter -= 1
