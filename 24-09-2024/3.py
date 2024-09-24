def klarge(nums,k):
    if not nums:
        return -1
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j],nums[i]
    return nums[-k:]

nums = list(map(int,input().split()))
k = 3
print(klarge(nums,k))