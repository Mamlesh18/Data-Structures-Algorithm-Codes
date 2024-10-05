def product(nums):
    if not nums:
        return 0
    result1 = []
    result2 = []
    for i in range(0,len(nums)):
        temp = 1
        for j in range(i+1,len(nums)):
            temp*=nums[j]
        result1.append(temp)
    for i in range(len(nums)-1,-1,-1):
        temp = 1
        for j in range(i):
            temp*=nums[j]
        result2.append(temp)
    result2 = result2[::-1]
    for i in range(0,len(result1)):
        result1[i] = result1[i] * result2[i]
    return result1

nums = [10, 3, 5, 6, 2]
print(product(nums))