def divisible(nums):
    if nums % 9 == 0:
        return True
    else:
        return False
n = int(input())
print(divisible(n))