def sums(nums,k):
    if not nums:
        return 0
    result = []
    for i in range(0,len(nums)-2):
        if i > 0 and nums[i] == nums[i+1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total == k:
                result.append([nums[left],nums[right],nums[i]])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left-1]:
                    left+=1
                while left < right and nums[right] == nums[right+1]:
                    right+=1
            elif total < k:
                left+=1
            else:
                right-=1
    return result
nums = [1,2,3,4,5]
k = 12
print(sums(nums,k))