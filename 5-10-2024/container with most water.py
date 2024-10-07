def container(nums):
    maxi = 0
    i = 0
    j = len(nums)-1
    while i < j:
        maxi = max(maxi, i-j * min(nums[i],nums[j]))
        if nums[i] < nums[j]:
            i+=1
        else:
            j-=1
    return maxi