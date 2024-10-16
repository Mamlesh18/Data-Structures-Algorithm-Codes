def rotate(nums,k):
    if not nums:
        return 0
    k = k % len(nums)
    res = nums[-k:] + nums[:-k]
    return res
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))