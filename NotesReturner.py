AmOwed = int(input("Insert the Amount Owed: "))
AmPaid = int(input("Insert the Amount Paid: "))
AmOwed = AmPaid - AmOwed
RemainingOwed = AmOwed

print("Balance: ", RemainingOwed)
print("-------------------")

notesOwed = int(RemainingOwed / 50)
RemainingOwed = RemainingOwed % 50
if notesOwed >= 1:
	print("50s: ", notesOwed)

notesOwed = int(RemainingOwed / 20)
RemainingOwed = RemainingOwed % 20
if notesOwed >= 1:
	print("20s: ", notesOwed)

notesOwed = int(RemainingOwed / 10)
RemainingOwed = RemainingOwed % 10
if notesOwed >= 1:
	print("10s: ", notesOwed)

notesOwed = int(RemainingOwed / 5)
RemainingOwed = RemainingOwed % 5
if notesOwed >= 1:
	print("5s: ", notesOwed)

notesOwed = int(RemainingOwed / 2)
RemainingOwed = RemainingOwed % 2
if notesOwed >= 1:
	print("2s: ", notesOwed)

notesOwed = int(RemainingOwed / 1)
RemainingOwed = RemainingOwed % 1
if notesOwed >= 1:
	print("1s: ", notesOwed)

if RemainingOwed > 0:
	print("An Error Occured!")