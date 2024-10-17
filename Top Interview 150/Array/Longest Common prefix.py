def long(nums):
    if not nums:
        return 0
    maxi = max(nums)
    minp = min(nums)
    result = ''
    for i in range(0,len(minp)):
        if minp[i] == maxi[i]:
            result+=maxi[i]
        else:
            break
    return result

nums = ["flower","flow","flight"]
print(long(nums))