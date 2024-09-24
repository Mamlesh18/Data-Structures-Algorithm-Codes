def spiral(nums):
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    top = 0
    bottom = len(nums[0]) -1
    result = []
    while left <= right and top <= bottom:
        for i in range(left,right+1):
            result.append(nums[top][i])
        top+=1

        for i in range(top,bottom+1):
            result.append(nums[i][right])
        right-=1

        for i in range(right,left-1,-1):
                result.append(nums[bottom][i])
        bottom-=1

        for i in range(bottom,top-1,-1):
                result.append(nums[i][left])
        left+=1
    return result

mat = int(input('rows'))
result = []
for i in range(mat):
    lists = list(map(int,input().split()))[:mat+1]
    result.append(lists)
print(spiral(result))
