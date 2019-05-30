def SplitWordsIntoList(String):
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

FileToEdit = input("Enter the File Name of A File To Edit:")
File_R = open(FileToEdit,"r")
File_W = open("DuplicatesRemoved"+FileToEdit,"w")
FinishedString = ""
PreviousWords = []

for Line in File_R:
	WordList = SplitWordsIntoList(Line)
	for Word in WordList:
		MatchFound = False
		for DupeWord in PreviousWords:
			if Word == DupeWord:
				MatchFound = True

		if MatchFound == False:
			PreviousWords.append(Word)
			FinishedString += Word + " "

	print(FinishedString,file=File_W)
	FinishedString = ""


	

