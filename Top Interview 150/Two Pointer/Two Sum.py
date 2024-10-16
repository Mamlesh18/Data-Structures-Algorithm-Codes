def towsum(nums,target):
    if not nums:
        return 0
    result = []
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            result.append(left+1)
            result.append(right+1)
            left+=1
            right-=1
            while left < right and nums[left] == nums[left-1]:
                left+=1
            while left<right and nums[right] == nums[right+1]:
                right-=1
        elif total < left:
            left+=1
        else:
            right-=1
    return result
nums = [2,7,11,15]
target = 9

print(towsum(nums,target))
