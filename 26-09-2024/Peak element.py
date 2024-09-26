def peak(nums):
    if not nums:
        return 0

    if nums[0] > nums[1]:
        return nums[i]
    if nums[-1] > nums[-2]:
        return nums[-1]
    for i in range(1,len(nums)-1):
        if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
            return nums[i]
    return False
nums = list(map(int,input().split()))
print(peak(nums))