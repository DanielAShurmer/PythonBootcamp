PName = input("Enter Name of Product: ")
PPrice = input("Enter Price of Product: ")
PQTY = input("Enter Amount of Products Purchased: ")
Amount = int(PQTY) * float(PPrice)
VAT = Amount * 15/100
Bill = Amount + VAT
print("Your Bill")
print("Product Purchased: ",PName)
print("Amount Purchased: ",PQTY)
print("VAT Added: £",VAT)
print("Total Cost: £",Bill)