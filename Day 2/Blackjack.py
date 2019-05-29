FirstNumber = int(input("Enter 1st Number:"))
SecondNumber = int(input("Enter 2nd Number:"))
Max = 0

if FirstNumber <= 21:
	Max = FirstNumber

if SecondNumber <= 21:
	if SecondNumber > Max:
		Max = SecondNumber
	elif SecondNumber == FirstNumber:
		Max = "Both Are Equal"

if Max == 0:
	Max = "Both Are Above 21"

print("The winning number is:",Max)
	