def mins(nums):
    if not nums:
        return []
    result = []
    for i in range(0,len(nums)):
        temp = 0
        for j in range(i,len(nums[0])):
            if nums[i][j] == 1:
                temp +=1
        result.append(temp)

    return result.index(min(result))
nums = [[1,0,1],[0,0,0],[1,1,1]]
print(mins(nums))

