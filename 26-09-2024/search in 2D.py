def searchin2d(nums,k):
    if not nums:
        return 0
    for i in range(0,len(nums)):
        for j in range(0,len(nums[0])):
            if nums[i][j] == k:
                return True
    return False
nums = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
print(searchin2d(nums,k))