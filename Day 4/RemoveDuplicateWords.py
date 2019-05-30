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

InputString = input("Enter A Message:")
WordList = SplitWordsIntoList(InputString)
Count = 0
FinishedString = ""
PreviousWords = []

while Count < len(WordList):
	#Identify if a word is in the duplicates list
	SubCount = 0
	MatchFound = False
	while SubCount < len(PreviousWords):
		if WordList[Count] == PreviousWords[SubCount]:
			MatchFound = True
		SubCount += 1

	#If it isn't, add it to the output string & duplicates list
	if MatchFound == False:
		PreviousWords.append(WordList[Count])
		FinishedString += WordList[Count] + " "

	Count += 1

print(FinishedString)