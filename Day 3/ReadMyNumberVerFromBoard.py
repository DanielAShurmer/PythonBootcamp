def ones(InputNum):
	Result = ""
	if InputNum == 1:
		Result = "One"
	if InputNum == 2:
		Result = "Two"
	if InputNum == 3:
		Result = "Three"
	if InputNum == 4:
		Result = "Four"
	if InputNum == 5:
		Result = "Five"
	if InputNum== 6:
		Result = "Six"
	if InputNum == 7:
		Result = "Seven"
	if InputNum == 8:
		Result = "Eight"
	if InputNum == 9:
		Result = "Nine"
	if InputNum== 10:
		Result = "Ten"
	if InputNum == 11:
		Result = "Eleven"
	if InputNum == 12:
		Result = "Twelve"
	if InputNum == 13:
		Result = "Thirteen"
	if InputNum == 14:
		Result = "Fourteen"
	if InputNum == 15:
		Result = "Fifteen"
	if InputNum== 16:
		Result = "Sixteen"
	if InputNum == 17:
		Result = "Seventeen"
	if InputNum == 18:
		Result = "Eighteen"
	if InputNum == 19:
		Result = "Nineteen"
	return Result

def tens(InputNum):
	Result = ""
	if InputNum == 20:
		Result = "Twenty"
	if InputNum == 30:
		Result = "Thirty"
	if InputNum == 40:
		Result = "Fourty"
	if InputNum == 50:
		Result = "Fifty"
	if InputNum == 60:
		Result = "Sixty"
	if InputNum == 70:
		Result = "Seventy"
	if InputNum == 80:
		Result = "Eighty"
	if InputNum == 90:
		Result = "Ninety"
	return Result

num = int(input("Enter Any Number:"))
Answer = ""

if num >= 1000 and num <= 9999:
	Answer += ones(int(num/1000)) + " Thousand "
	num %= 1000

if num >= 100:
	Answer += ones(int(num/100)) + " Hundred "
	num %= 100

if num >= 20:
	Answer += tens(int(num/10)*10) + " "
	num %= 10

if num > 0 and num <= 19:
	Answer += ones(num)
	
print(Answer)