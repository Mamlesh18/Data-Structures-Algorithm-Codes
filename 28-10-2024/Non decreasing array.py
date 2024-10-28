def nondecreasing(nums):
    if not nums:
        return False
    temp = False
    count = 0
    for i in range(1,len(nums)):

        if nums[i] < nums[i-1]:
            if temp:
                return False
            if i == 1 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
            temp = True


    return True


nums = [4,2,1]
print(nondecreasing(nums))