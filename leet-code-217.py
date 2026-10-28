nums = [1,2,3,1]

for i in range(0,len(nums)):
	j = i
	if i!=j and nums[i] == nums[j]:
		return False