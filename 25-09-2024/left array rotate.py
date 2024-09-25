def left(nums,k):
    if not nums:
        return 0
    k = k % len(nums)

    mat = nums[k:] + nums[:k]

    return mat

nums = list(map(int,input().split()))
k = int(input())
print(left(nums,k))

