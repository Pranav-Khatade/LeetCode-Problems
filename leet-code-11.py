height = [1,8,6,2,5,4,8,3,7]
r = len(height)-1
l = 0
area = 0
while l<r:
    current = min(height[l],height[r])*abs(l-r)
    area = max(current, area)

    if height[l]<height[r]:
        l +=1
    else:
        r -= 1
print(area)