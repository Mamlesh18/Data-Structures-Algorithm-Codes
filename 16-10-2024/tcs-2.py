def matrix(nums):
    if not nums:
        return 0
    top = 0
    mid = len(nums)//2
    result = []
    while top < len(nums[0]):
        for i in range(len(nums)-1,-1,-1):
            result.append(nums[i][top])
        for j in range(mid,len(nums)):
            result.append(nums[j][top])
        top+=1
    return result
nums = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(matrix(nums))

