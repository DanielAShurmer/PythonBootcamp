def StrToList(String):
	StringLen = len(String)
	Counter = 0
	OutList = []
	while Counter < StringLen:
		OutList.append(String[Counter])
		Counter += 1
	return OutList

def FindAndReplace(String,Find,Replace):
	InputList = StrToList(String)

	FindLength = len(Find)
	Counter = 0

	while Counter < len(String):
		if String[Counter:Counter+FindLength] == Find:
			




InputString = input("Enter A String:")
StringToFind = input("Enter A Substring To Find:")
StringToReplace = input("Enter A Substring To Replace With:") 

print(FindAndReplace(InputString,StringToFind,StringToReplace))