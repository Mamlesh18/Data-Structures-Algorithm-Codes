def sums(nums):
    result =0
    i = 0
    while i < len(nums):
        result+=nums[i]
        i+=1
    return result
n = list(map(int,input().split()))
print(sums(n))