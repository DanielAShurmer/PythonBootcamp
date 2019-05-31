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

def FindLongest(String):
	WordList = SplitWordsIntoList(String)
	MaxFound = 0
	WordFound = []

	for Word in WordList:
		if len(Word) == MaxFound:
			WordFound.append(Word)
		if len(Word) > MaxFound:
			MaxFound = len(Word)
			WordFound = [Word]

	return [MaxFound,WordFound]

InputString = input("Please Enter A Message:")
Output = FindLongest(InputString)

print("The Longest Word(s), With A Length Of",Output[0],"Is:")
for Word in Output[1]:
	print(Word)

