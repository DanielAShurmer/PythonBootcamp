def CountAlpha(message,alpha):
	Looper = 0
	Count = 0
	while Looper < len(message):
		if message[Looper].upper() == alpha:
			Count += 1
		Looper += 1
	if Count > 0:
		print(alpha,"=",Count)

InputMessage = input("Enter Any Message")
CurrentChar = 65
while CurrentChar <= 90:
	CountAlpha(InputMessage,chr(CurrentChar))
	CurrentChar += 1