def jump(nums):
    if not nums:
        return 0
    count = 0
    i = 0
    while i < len(nums):
        count = max(nums[i]+i,count)
        if count == len(nums):
            return True
        if nums[i] == 0:
            return False
        i+=1
    return False


nums = [2,3,1,1,1]
print(jump(nums))