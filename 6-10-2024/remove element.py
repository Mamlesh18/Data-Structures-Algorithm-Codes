def remove(nums,k):
    i = 0
    while i < len(nums):
        if nums[i] == k:
            nums.pop(i)
        else:
            i+=1
    return nums
nums = [3,2,2,3]
k = 2
print(remove(nums,k))