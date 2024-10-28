def longest(nums):
    if not nums:
        return 0
    count = 1
    temp = 0
    for i in range(0,len(nums)-1):
        if nums[i] < nums[i+1]:
            count+=1
        else:
            temp = max(temp,count)
            count = 1
    temp = max(temp,count)
    return temp
nums = [1,3,5,4,2,3,4,5]


print(longest(nums))
