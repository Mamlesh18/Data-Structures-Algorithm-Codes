def stock(nums):
    if not nums:
        return 0
    minp = nums[0]
    maxp = 0
    for i in nums:
        minp = min(minp,i)
        profit = i - minp
        maxp = max(maxp,profit)
    return maxp

nums = [7, 10, 1, 3, 6, 9, 2]
print(stock(nums))