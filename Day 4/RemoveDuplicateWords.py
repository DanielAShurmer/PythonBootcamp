def SplitWordsIntoList(String):
	#Or Code A
	OutList = []
	CurrentWord = ""
	for Character in String:
		if Character == " ":
			OutList.append(CurrentWord)
			CurrentWord = ""
		else:
			CurrentWord += Character
	OutList.append(CurrentWord)
	return OutList  


InputString = input("Enter A Message:")
WordList = SplitWordsIntoList(InputString)
FinishedString = ""
PreviousWords = []

#Or Code B
for Word in WordList:
	MatchFound = False
	for DupeWord in PreviousWords:
		if Word == DupeWord:
			MatchFound = True

	if MatchFound == False:
		PreviousWords.append(Word)
		FinishedString += Word + " "

print(FinishedString)

#Code A
'''StringLen = len(String)
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
	return OutList'''

#Code B
	'''
Count = 0

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
'''