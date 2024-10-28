def house(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return max(nums[0],nums[1])

    j = 1
    count1 = 0
    count2 = 0
    for i in range(0,len(nums)):
        if i % 2 == 0:
            count1+=nums[i]

            i+=2
        else:
            count2+=nums[j]
            j+=2
    return max(count2,count1)
nums = [1,3,5,2,5]
print(house(nums))