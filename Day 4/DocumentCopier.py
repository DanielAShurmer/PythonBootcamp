File_R = open("File.txt","r")
File_W = open("CopiedFile.txt","w")
for Line in File_R:
	print(Line,file=File_W)

print("Document ",end="")
print("Copied")
