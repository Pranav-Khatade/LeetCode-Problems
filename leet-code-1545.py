s = '0'
n =4
lp1 = ['0']
k = 11
for i in range(1,n):
	p = ''.join(reversed(s))
	inv = ''
	for j in p:
		if j =='1':
			inv += '0'
		elif j == '0':
			inv += '1'
	s = s + "1" + inv
	lp1.append(s)
kth = lp1[n-1]
kp = kth[k-1]
print(kp)