def stock(nums):
    if not nums:
        return 0
    maxp = 0
    for i in range(0,len(nums)-1):
        if nums[i] < nums[i+1]:
            maxp+= nums[i+1] - nums[i]
    return maxp

nums = [1,2,3,4,5]
print(stock(nums))