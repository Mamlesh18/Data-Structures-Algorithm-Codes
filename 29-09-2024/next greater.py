def next(nums):
    if not nums:
        return 0
    result = []
    for i in range(0,len(nums)):
        found = False
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                found = True
                result.append(nums[j])
                break
        if not found:
            result.append(-1)

    return result

nums = list(map(int,input().split()))
print(next(nums))