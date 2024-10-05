def two(nums,k):
    if not nums:
        return 0
    nums.sort()
    result = []
    i = 0
    j = len(nums)-1
    while i < j:
        total = nums[i] + nums[j]
        if total == k:
            result.append([nums[i],nums[j]])
            i+=1
            j-=1
            while i < j and nums[i] == nums[i-1]:
                i+=1
            while i < j and nums[j] == nums[j+1]:
                j-=1
        elif total < k:
            i+=1
        else:
            j-=1
    return result
nums = list(map(int,input().split()))
k = int(input())
print(two(nums,k))