prices = [7,6,4,3,1]

profit = 0
mp = prices[0]
for i in range(0,len(prices)):
	profit = max(profit, prices[i]-mp)
	mp = min(mp,prices[i])
print(profit)