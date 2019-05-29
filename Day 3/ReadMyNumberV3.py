ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]

num = int(input("Enter Any Number:"))
Answer = ""

if num >= 1000 and num <= 9999:
	Answer += ones[int(num/1000)] + " Thousand "
	num %= 1000

if num >= 100:
	Answer += ones[int(num/100)] + " Hundred "
	num %= 100

if num >= 20:
	Answer += tens[int(num/10)] + " "
	num %= 10

if num > 0 and num <= 19:
	Answer += ones[num]
	
print(Answer)