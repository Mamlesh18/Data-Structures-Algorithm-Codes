def long(nums1,nums2):
    if not nums1 or not nums2:
        return 0
    result1 = []
    result2 = []
    for i in range(2**len(nums1)):
        sub = ''
        for j in range(len(nums1)):
            if (i & (1<<j)) > 0:
                sub+=nums1[j]
        result2.append(sub)
    for i in range(2**len(nums2)):
        sub = ''
        for j in range(len(nums2)):
            if (i &(1<<j)) > 0:
                sub+=nums2[j]
        result1.append(sub)
    res = ''
    for i in range(1,len(result2)):
        if result2[i] in result1 and len(result2[i]) > len(res) :
            res = result2[i]
    return res
nums1 = 'AGGTAB'
nums2 = 'GXTXAYB'
print(long(nums1,nums2))