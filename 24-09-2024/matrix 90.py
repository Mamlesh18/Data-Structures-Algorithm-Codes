def matrix(nums):
    if not nums:
        return 0
    top = 0
    bottom = len(nums[0])-1
    while top < bottom:
        for i in range(0,len(nums)):
            temp = nums[top][i]
            nums[top][i] = nums[bottom][i]
            nums[bottom][i] = temp
        top+=1
        bottom-=1

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            temp = nums[i][j]
            nums[i][j] = nums[j][i]
            nums[j][i] = temp
    return nums
n = int(input("rows"))
mat = []
for i in range(n):
    lists = list(map(int,input().split()))[:n+1]
    mat.append(lists)
print(matrix(mat))

