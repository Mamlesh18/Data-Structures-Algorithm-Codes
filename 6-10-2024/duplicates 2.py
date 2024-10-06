def duplit(nums):
    if not nums:
        return 0
    dicts = {}
    for i in range(0,len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]] +=1
        else:
            dicts[nums[i]] = 1

    result = []
    for u,v in dicts.items():
        if v > 2:
            result.extend([u] * 2)
        else:
            result.extend([u] * v)
    return result
nums = [1,1,1,2,2,3]
print(duplit(nums))