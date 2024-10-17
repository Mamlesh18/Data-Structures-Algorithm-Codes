def container(nums):
    if not nums:
        return 0
    maximum = 0
    i = 0
    j = len(nums)-1
    while i < j:
        maximum = max(maximum,(j-i) * min(nums[i],nums[j]))
        if nums[i] < nums[j]:
            i+=1
        else:
            j-=1
    return maximum
nums = [1,8,6,2,5,4,8,3,7]
print(container(nums))