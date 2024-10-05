def house(nums):
    if not nums:
        return 0
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    currsum1 = 0
    currsum2 = 0
    for i in range(0,len(nums)):
        if i % 2 == 0:
            currsum1+=nums[i]
        else:
            currsum2+=nums[i]
    return max(currsum2,currsum1)

nums = [6, 7, 1, 3, 8, 2, 4]
print(house(nums))

