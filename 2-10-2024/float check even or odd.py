def floating(nums):
    s = nums.rstrip('0')
    last = s[-1]
    if int(last) % 2== 0:
        return True
    else:
        return False
n = input()
print(floating(n))