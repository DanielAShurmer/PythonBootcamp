Words = 0
MSG = input("Enter A Message:")
Counter = 0
while Counter < len(MSG):
	if MSG[Counter] == " ":
		Words += 1
	Counter += 1
print("There are", (Words + 1), "words in your message.")