def indexofsub(nums,k):
    current = 0
    left = 0
    right = 0
    while right <= len(nums):
        current+=nums[right]
        while current > k and left <= right:
            current-=nums[left]
            left+=1
        if current == k:
            return left,right
        right+=1
nums = list(map(int,input().split()))
k = int(input())
print(indexofsub(nums,k))
