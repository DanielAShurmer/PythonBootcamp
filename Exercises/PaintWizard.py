import time
print("---------PAINT-WIZARD---------")

InputArea = int(input("""Enter the total surface area you want to paint, 
	in Meters Squared - round up to the nearest whole number: """))

CheapoMaxAreaPerCan = 20 * 10
AverageJoesAreaPerCan = 15 * 11
DuluxPaintsAreaPerCan = 10 * 20

CheapoMaxLitresNeeded = InputArea / 10
AverageJoesLitresNeeded = InputArea / 11
DuluxPaintsLitresNeeded = InputArea / 20

CheapoMaxCansNeeded = int(InputArea / CheapoMaxAreaPerCan) + 1
AverageJoesCansNeeded = int(InputArea / AverageJoesAreaPerCan) + 1
DuluxPaintsCansNeeded = int(InputArea / DuluxPaintsAreaPerCan) + 1

CheapoMaxPrice = CheapoMaxCansNeeded * 19.99
AverageJoesPrice = AverageJoesCansNeeded * 17.99
DuluxPaintsPrice = DuluxPaintsCansNeeded * 25.00 

CheapoMaxSpareLitres = 20 - (CheapoMaxLitresNeeded % 20)
AverageJoesSpareLitres = 15 - (AverageJoesLitresNeeded % 15)
DuluxPaintsSpareLitres = 10 - (DuluxPaintsLitresNeeded % 10)

if CheapoMaxSpareLitres == 20.0:
	CheapoMaxSpareLitres = 0.0

if AverageJoesSpareLitres == 15.0:
	AverageJoesSpareLitres = 0.0

if DuluxPaintsSpareLitres == 10.0:
	DuluxPaintsSpareLitres = 0.0

MinWaste = CheapoMaxSpareLitres
MinWasteName = "Cheapo Max"
if AverageJoesSpareLitres < MinWaste:
	MinWaste = AverageJoesSpareLitres
	MinWasteName = "Average Joes"
if DuluxPaintsSpareLitres < MinWaste:
	MinWaste = DuluxPaintsSpareLitres
	MinWasteName = "Duluxourous Paints"

MinPrice = CheapoMaxPrice
MinPriceName = "Cheapo Max"
if AverageJoesPrice < MinPrice:
	MinPrice = AverageJoesPrice
	MinPriceName = "Average Joes"
if DuluxPaintsPrice < MinPrice:
	MinPrice = DuluxPaintsPrice
	MinPriceName = "Duluxourous Paints"

print("\n")
print("Thinking...")
time.sleep(2)
print("Pulling Answer From Hat...")
time.sleep(2)
print("Summoning Solution...")
time.sleep(2)

print("The Least Wasted Paint Will Be From Purchasing", MinWasteName, "With Just", MinWaste, "Litres Of Paint Wasted") 

print("\n")
print("Washing Magic Brushes...")
time.sleep(2)
print("Consulting Tomes...")
time.sleep(2)
print("Summoning Solution...")
time.sleep(2)

print("The Cheapest Paint To Use Is", MinPriceName, "Which Will Cost £", MinPrice) 