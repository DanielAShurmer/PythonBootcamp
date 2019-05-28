TimesTable = int(input("Enter Times Table to Calculate:"))
TillValue = int(input("Enter Value To Times Up Until:"))
Count = 1
while Count <= TillValue:
    print(TimesTable,"X",Count,"=",(TimesTable * Count))
    Count += 1