def majorityElement(nums):
    if len(nums) == 1:
        return nums
    result = []
    dicts = {}
    for i in range(0, len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]] += 1
        else:
            dicts[nums[i]] = 1
    ele = len(nums) // 3
    for u, v in dicts.items():
        if v > ele:
            result.append(u)
    return result
nums = list(map(int,input().split()))
print(majorityElement(nums))
