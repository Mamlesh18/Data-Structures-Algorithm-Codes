def merge(nums1,m,nums2,n):

    for i in range(0,n):
        nums1[m] = nums2[i]
        m +=1
    return nums1

nums1 = [1]
m = 1
nums2 = []
n = 0
print(merge(nums1,m,nums2,n))