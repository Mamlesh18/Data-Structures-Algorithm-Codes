def maxi(nums):
    if not nums:
        return 0
    res = [0,0]
    ind = -1
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i]-nums[j]) > abs(res[0] - res[1]) and j >= ind:
                res = [nums[i],nums[j]]
                ind = j
    return res,ind

nums = list(map(int,input().split()))
print(maxi(nums))