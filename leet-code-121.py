prices = [7,1,5,3,6,4]
k = 0
while(k<len(prices)):
	for i in range(k,len(prices)):
		profit = max(prices[k],prices[i]-prices[k])
	k=k+1

if profit<0:
	print("0")
else:
	print(profit)