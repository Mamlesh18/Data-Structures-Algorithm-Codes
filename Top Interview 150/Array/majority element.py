def major(nums):
    if not nums:
        return 0
    dicts = {}
    for i in range(0,len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]] += 1
        else:
            dicts[nums[i]] = 1
    sorte = sorted(dicts.items(),key = lambda item:item[1],reverse=True)
    return sorte[0][0]
nums = [3,3,3,2,2]
print(major(nums))
