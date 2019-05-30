def SplitWordsIntoList(String):
	StringLen = len(String)
	Counter = 0
	OutList = []
	CurrentWord = ""
	while Counter < StringLen:
		if String[Counter] == " ":
			OutList.append(CurrentWord)
			CurrentWord = ""
		else:
			CurrentWord += String[Counter]
		Counter += 1
	OutList.append(CurrentWord)
	return OutList

def ReverseWord(String):
	StringLen = len(String)
	Counter = StringLen - 1
	OutWord = ""
	while Counter >= 0:
		OutWord += String[Counter]
		Counter -= 1
	return OutWord


InputString = input("Enter A Message:")
WordList = SplitWordsIntoList(InputString)
Count = 0
FinishedString = ""

while Count < len(WordList):
	FinishedString += ReverseWord(WordList[Count]) + " "
	Count += 1

print(FinishedString)