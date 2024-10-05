def water(nums):
    if not nums:
        return 0
    left = 0
    right = len(nums)-1
    maxi = 0
    while left < right:
        width = right - left
        height = min(nums[left],nums[right])
        curr = width * height

        maxi = max(maxi,curr)

        if nums[left] < nums[right]:
            left+=1
        else:
            right-=1
    return maxi

nums = [3,1,2,4,5]
print(water(nums))