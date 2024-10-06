def jump(nums):
    if not nums:
        return False
    count = 0
    i = 0
    while i < len(nums):
        count = max(nums[i]+i,count)
        if count >= len(nums):
            return True
        if nums[i] == 0 or count == i:
            return False
        i+=1
    return False


nums = [3,2,1,1,4]
print(jump(nums))
