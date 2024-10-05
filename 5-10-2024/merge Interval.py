def merge(nums):
    if not nums:
        return []
    nums = sorted(nums,key = lambda item:item[0])
    result=[]
    temp = nums[0]
    for i in range(1,len(nums)):
        if temp[1] >= nums[i][0]:
            temp[1] = max(temp[1],nums[i][1])
        else:
            result.append(temp)
            temp = nums[i]
    result.append(temp)
    return result

nums = [[1,3],[2,4],[6,8],[9,10]]
print(merge(nums))