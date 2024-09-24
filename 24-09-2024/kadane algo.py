def kadane(nums):
    if not nums:
        return 0
    current = nums[0]
    maximum = nums[0]
    for i in range(1,len(nums)):
        current = max(nums[i],current+nums[i])
        maximum = max(maximum,current)

    return maximum



nums = list(map(int,input().split()))
print(kadane(nums))