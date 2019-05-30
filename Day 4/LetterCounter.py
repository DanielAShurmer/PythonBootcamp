Alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
AlphaCap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
InputMessage = input("Enter A Message:")
LoopCount = 0

while LoopCount < len(InputMessage):
	if ord(InputMessage[LoopCount]) >= 65 and ord(InputMessage[LoopCount]) <= 90:
		Alpha[ord(InputMessage[LoopCount]) - 65] += 1

	if ord(InputMessage[LoopCount]) >= 97 and ord(InputMessage[LoopCount]) <= 122:
		AlphaCap[ord(InputMessage[LoopCount]) - 97] += 1

	LoopCount += 1

LoopCount = 0

while LoopCount <= 25:
	if Alpha[LoopCount] > 0:
		print(chr(LoopCount+65),"=",Alpha[LoopCount])
	if AlphaCap[LoopCount] > 0:
		print(chr(LoopCount+97),"=",AlphaCap[LoopCount])

	LoopCount += 1