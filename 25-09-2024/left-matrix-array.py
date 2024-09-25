def matrix(nums,k):
    if not nums:
        return []
    k = k % len(nums[0])
    result = []
    for i in nums:
        mats = i[k:] + i[:k]
        result.append(mats)
    return result



n = int(input("enter row"))
res = []
for i in range(n):
    mat = list(map(int,input().split()))
    res.append(mat)
k = int(input())
print(matrix(res,k))