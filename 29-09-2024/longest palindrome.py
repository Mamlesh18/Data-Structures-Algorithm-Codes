def long(nums):
    if not nums:
        return None
    maxi = 0
    result = 0
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            total = nums[i:j+1]
            if plaicheck(total) and len(total) > maxi:
                maxi = len(total)
                result = nums[i:j+1]
    return result,maxi

def plaicheck(nums):
    if nums == nums[::-1]:
        return True
    else:
        return False

nums = input('enter str')
print(long(nums))