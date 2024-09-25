def nextgreater(nums):
    if not nums:
        return 0

    result = []
    for i in range(0,len(nums)):
        temp = False
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                result.append(nums[j])
                temp = True
                break
        if not temp:
            result.append(-1)
    result.append(-1)

    return result

nums = list(map(int,input().split()))
print(nextgreater(nums))