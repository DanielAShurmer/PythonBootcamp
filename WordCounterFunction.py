def WordCounter(MSG):
	Words = 0
	Counter = 0
	while Counter < len(MSG):
		if MSG[Counter] == " ":
			Words += 1
		Counter += 1
	return Words + 1

while True:
	InputMessage = input("Please Enter A Message, or Enter 'Exit' to Exit:")
	if InputMessage == "Exit":
		break
	print("There are",WordCounter(InputMessage),"words in your message.")