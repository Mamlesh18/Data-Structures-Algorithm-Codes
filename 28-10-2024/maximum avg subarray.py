def maximum(nums,k):
    maxi = 0
    for i in range(0,len(nums)-k+1):
        total = sum(nums[i:i+k])/k,5

        maxi = max(total,maxi)
    return maxi


nums =  [-1]
k = 1
print(maximum(nums,k))