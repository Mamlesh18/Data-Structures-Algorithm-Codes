def conse(nums):

    nums1 = list(set(nums))
    nums1.sort()
    result = 1
    long = 1
    for i in range(0,len(nums1)-1):
        if nums1[i] == nums1[i+1] - 1:
            result+=1
        else:
            long = max(long,result)
            result = 1
    long = max(long,result)
    return long


nus = [9,5,4,9,10,10,6]
print(conse(nus))