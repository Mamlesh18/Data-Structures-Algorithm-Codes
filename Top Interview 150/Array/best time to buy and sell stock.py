def stock(nums):
    if not nums:
        return 0
    maxp = 0
    minp = nums[0]
    for i in nums:
        minp = min(minp,i)
        profit = i - minp
        maxp = max(profit,maxp)
    return maxp
nums = [7,1,5,3,6,4]
print(stock(nums))
