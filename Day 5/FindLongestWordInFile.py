def SplitWordsIntoList(String):
	OutList = []
	CurrentWord = ""
	for Character in String:
		if Character == " ":
			OutList.append(CurrentWord)
			CurrentWord = ""
		else:
			if Character != "\n":
				CurrentWord += Character
	OutList.append(CurrentWord)
	print(OutList)
	return OutList

FileToEdit = input("Enter the File Name of A File To Examine:")
File_R = open(FileToEdit,"r")

MaxFound = 0
WordFound = []

for Line in File_R:
	WordList = SplitWordsIntoList(Line)
	for Word in WordList:
		if len(Word) == MaxFound:
			WordFound.append(Word)
		if len(Word) > MaxFound:
			MaxFound = len(Word)
			WordFound = [Word]

print("The Longest Word(s), With A Length Of",MaxFound,"Is:")
for Word in WordFound:
	print(Word)
