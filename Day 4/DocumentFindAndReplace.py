def StrToList(String):
	OutList = []
	for character in String:
		if Character != "\n":
			OutList.append(character)
	return OutList

def FindAndReplace(String,Find,Replace):
	InputList = StrToList(String)
	OutString = ""
	FindLength = len(Find)
	Counter = 0
	while Counter < len(String):
		if String[Counter:Counter+FindLength] == Find:
			Counter += FindLength
			OutString += Replace
		else:
			OutString += String[Counter]
			Counter += 1
	return OutString

FileToEdit = input("Enter the File Name of A File To Edit:")
File_R = open(FileToEdit,"r")
File_W = open("FindAndReplaced"+FileToEdit,"w")
StringToFind = input("Enter A Substring To Find:")
StringToReplace = input("Enter A Substring To Replace With:") 
for Line in File_R:
	if Line != "\n":
		print(FindAndReplace(Line,StringToFind,StringToReplace),file=File_W)
print("File Successfully Saved As: FindAndReplaced"+FileToEdit)