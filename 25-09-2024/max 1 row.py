def maxi(nums):
    if not nums:
        return []
    result = []
    for i in range(0,len(nums)):
        ones = 0
        for j in range(0,len(nums[0])):
            if nums[i][j] == 1:
                ones+=1

        result.append(ones)
    return result.index(max(result))

nums=  [[1,0,1],[1,1,1],[1,1,0]]
print(maxi(nums))

