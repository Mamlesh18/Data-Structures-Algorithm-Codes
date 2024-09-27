def sorting(nums):
    if not nums:
        return 0
    dicts = {}
    for i in range(0,len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]] +=1
        else:
            dicts[nums[i]] = 1
    result = []
    sort = sorted(dicts.items(),key= lambda item:item[0])
    for k,v in sort:
        result.extend([k]*v)
    return result

nums = list(map(int,input().split()))
print(sorting(nums))