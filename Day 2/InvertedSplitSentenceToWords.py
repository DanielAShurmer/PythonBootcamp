InputString = " " + input("Enter a Message:")
Word = ""
CorrectedWord = ""
Counter = len(InputString) - 1

while Counter >= 0:
	if InputString[Counter] ==  " ":

		SubCounter = len(Word) - 1
		while SubCounter >= 0:
			CorrectedWord += Word[SubCounter]
			SubCounter -= 1



		print(CorrectedWord)
		Word = ""
		CorrectedWord =""
	else:
		Word += InputString[Counter]
	Counter -= 1
