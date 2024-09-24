def sums4(nums, k):
    if not nums:
        return 0
    result = []
    nums.sort()

    for i in range(len(nums) - 3):
        # Changed to check with the previous element instead of the next
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            # Changed to check with the previous element instead of the next
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i] + nums[j]
                if total == k:
                    # Adjusted order of appending the result to match sorted nums
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < k:
                    left += 1
                else:
                    right -= 1

    return result


nums = [1, 2, 3, 4, 2, 2, 2, 2, 5, 7, 6, 5, 4, 32, 3, 5, 6, 2, 2, 1,1]
k = 6
print(sums4(nums, k))
