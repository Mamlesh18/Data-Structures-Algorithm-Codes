def insertion(nums):
    #TIME COMPLEXITY O N^2
    if not nums:
        return 0
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j], nums[i]
    return nums

nums = list(map(int,input('enteer n umber').split()))
print(insertion(nums))