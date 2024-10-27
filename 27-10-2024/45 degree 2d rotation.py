def rotation(nums):
    if not nums:
        return 0
    top = 0
    resut = []
    while top < len(nums):
        for i in range(len(nums)//2-1,-1,-1):
            resut.append(nums[i][top])
        for j in range(len(nums)//2,len(nums)):
            resut.append(nums[j][top])
        top+=1
    return resut

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotation(nums))