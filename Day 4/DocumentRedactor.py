File_R = open("File.txt","r")
File_W = open("RedactedFile.txt","w")
for Line in File_R:
	for Char in Line:
		if Char == "i" or Char == "I":
			print("*",file=File_W,end="")
		else:
			print(Char,file=File_W,end="")
