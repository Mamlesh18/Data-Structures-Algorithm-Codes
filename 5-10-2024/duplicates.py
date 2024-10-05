def duplicates(nums):
    if not nums:
        return None
    dicts = {}
    for i in range(0,len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]]+=1
        else:
            dicts[nums[i]] = 1
    result = []
    for u,v in dicts.items():
        if v > 1:
            result.append(u)
    return result


nums = list(map(int,input().split()))
print(duplicates(nums))