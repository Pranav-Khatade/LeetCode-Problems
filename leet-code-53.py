nums = [-2,1,-3,4,-1,2,1,-5,4]
total = 0
for i in range(len(nums),0):
	if nums[i] >= 0:
		total = total + nums[i]
	else:
		continue
print(total)