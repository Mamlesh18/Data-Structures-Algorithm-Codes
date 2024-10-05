def interval(nums,k):
    if not nums:
        return None
    nums.append(k)
    nums = sorted(nums,key = lambda item:item[0])
    result = []
    temp = nums[0]
    for i in range(1,len(nums)):
        if temp[1] >= nums[i][0]:
            temp[1] = max(nums[i][1],temp[1])
        else:
            result.append(temp)
            temp = nums[i]
    result.append(temp)
    return result

nums = [[1,3],[6,9]]
new = [2,5]
print(interval(nums,new))