def products(nums):
    if not nums:
        return 0
    result1 = []
    for i in range(0,len(nums)):
        temp = 1
        for j in range(i+1,len(nums)):
            temp*=nums[j]
        result1.append(temp)
    result2 = []
    for a in range(len(nums)-1,-1,-1):
        temp=1
        for b in range(a):
            temp*=nums[b]
        result2.append(temp)
    rev = result2[::-1]
    total = []
    for i in range(0,len(nums)):
        total.append(result1[i] * rev[i])
    return total

nums = [-1,1,0,-3,3]
print(products(nums))