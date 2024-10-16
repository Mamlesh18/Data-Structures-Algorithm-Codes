def removes(nums,val):
    if not nums:
        return 0
    result = []
    i = 0
    while i < len(nums):
        if nums[i] != val:
            result.append(nums[i])
        i+=1
    return result
nums = [3,2,2,3]
val = 3
print(removes(nums,val))