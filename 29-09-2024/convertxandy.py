def converts(nums):
    if not nums:
        return 0
    count = 0
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            count+=1
            if nums[i-1] == 'x':
                nums.replace(nums[i-1],'y')
            else:
                nums.replace(nums[i-1],'x')
    return count,nums


nums = input("message-> ")
print(converts(nums))