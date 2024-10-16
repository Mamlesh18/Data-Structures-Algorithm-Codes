def mergesor(nums1,nums2,m,n):
    if not nums2:
        return nums1
    i = 0
    for j in range(m,m+n):
        nums1[j] = nums2[i]
        i+=1
    return nums1
nums1 = [1]
nums2 = [0]
m = 1
n = 0
print(mergesor(nums1,nums2,m,n))
