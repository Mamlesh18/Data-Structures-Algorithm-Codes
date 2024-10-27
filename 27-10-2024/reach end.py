def end(nums):
    if not nums:
        return 0
    count = 0
    i = 0
    while i < len(nums):
        i+=nums[i]
        count+=1
    return count
nums = [1,2,3,4,5]
print(end(nums))