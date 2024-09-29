def converts(nums):
    if not nums:
        return 0,nums
    count = 0
    result = list(nums)
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            count+=1
            if result[i-1] == 'x':
                result[i-1] = 'y'
            else:
                result[i-1] = 'x'
    return count, ''.join(result)


nums = input("message-> ")
print(converts(nums))