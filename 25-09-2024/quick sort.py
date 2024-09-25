def quick(nums):

    if not nums:
        return []
    mid = len(nums)//2
    pivot = nums[mid]

    left_piv = [x for x in nums if x < pivot]
    mid_piv = [x for x in nums if x == pivot]
    right_piv = [x for x in nums if x > pivot]

    return quick(left_piv) + mid_piv + quick(right_piv)

nums = list(map(int,input().split()))
print(quick(nums))

