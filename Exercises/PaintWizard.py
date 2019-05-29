print("---------PAINT-WIZARD---------")

InputArea = int(input("""Enter the total surface area you want to paint, 
	in Meters Squared - round up to the nearest whole number: """))

CheapoMaxAreaPerCan = 20 * 10
AverageJoesAreaPerCan = 15 * 11
DuluxPaintsAreaPerCan = 10 * 20

CheapoMaxPricePerMeter = 19.99 / CheapoMaxAreaPerCan
AverageJoesPricePerMeter = 17.99 / AverageJoesAreaPerCan
DuluxPaintsPricePerMater = 25.00 / DuluxPaintsAreaPerCan

CheapoMaxLitresNeeded = InputArea / 10
AverageJoesLitresNeeded = InputArea / 11
DuluxPaintsLitresNeeded = InputArea / 20

CheapoMaxSpareLitres = 20 - (CheapoMaxLitresNeeded % 20)
AverageJoesSpareLitres = 15 - (AverageJoesLitresNeeded % 15)
DuluxPaintsSpareLitres = 10 - (DuluxPaintsLitresNeeded % 10)

print(CheapoMaxSpareLitres)
print(AverageJoesSpareLitres)
print(DuluxPaintsSpareLitres)


