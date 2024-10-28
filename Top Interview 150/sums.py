# Given an array of integers nums and a specific integer target, find and return the indices of the two numbers in the array that sum up to the target value.
# You can assume that there will always be exactly one solution, and the same element cannot be used twice. The order in which you return the indices does not matter.
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: The numbers at indices 0 and 1 (2 + 7) add up to the target value of 9.

def twosum(nums,target):
    if not nums:
        return -1
    result = []
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            result.append([left,right])
            left+=1
            right-=1
            while left < right and nums[left] == nums[left-1]:
                left+=1

            while left < right and nums[right] == nums[right+1]:
                right-=1
        elif total<target:
            left+=1
        else:
            right-=1
    return result

nums = [2,7,11,15]
target = 9
print(twosum(nums,target))


