Numbers = []

while True:
	Num = int(input("Enter a Number, Or Enter '0' to Stop:"))
	if Num == 0:
		break
	Numbers.append(Num)

Highest = Numbers[0]
Counter = 1
while Counter < len(Numbers):
	if Numbers[Counter] > Highest:
		Highest = Numbers[Counter]
	Counter += 1

print("The Highest Value You Entered Is:", Highest)