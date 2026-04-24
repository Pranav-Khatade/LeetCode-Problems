s = '0100'
li = list(s)
count1 = 0
count2 = 0
for i in range(len(li)):
	if li[i] != '0' and li[i+1] != str((i+1)%2 ):
		li[i] = '0'
		li[i+1] = str((i+1)%2)
	else:
		count1 += 1
	if li[i] != '1' and li[i+1] != str((i+1)%2) - '1':
		li[i] = '1'
		li[i+1] = str((i+1)%2 -1)
	else:
		count2 += 1
print(min(count1, count2))	  