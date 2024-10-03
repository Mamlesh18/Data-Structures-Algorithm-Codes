def minSubarray(nums, p):
    total = sum(nums)
    rem=total % p
    if rem ==0:
        return 0
    for i in range(0, len(nums)):
            a = nums[:i]
            b = sum(a)
            if b % p == 0:
                return (len(nums) - len(a))
nums = [3,1,4,2]
p = 6
print(minSubarray(nums,p))