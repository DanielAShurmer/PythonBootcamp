def StrToList(String):
	OutList = []
	for character in String:
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

InputString = input("Enter A String:")
StringToFind = input("Enter A Substring To Find:")
StringToReplace = input("Enter A Substring To Replace With:") 

print(FindAndReplace(InputString,StringToFind,StringToReplace))