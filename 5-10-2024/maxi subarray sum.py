def maxi(nums):
    if not nums:
        return 0
    maxim = 0
    currsum = 0
    for i in nums:
        currsum+=i
        if currsum < 0:
            currsum = 0
        maxim = max(maxim,currsum)
    return maxim
maxim = list(map(int,input().split()))
print(maxi(maxim))
