def pali(nums):

    return True if nums == nums[::-1] else False


n = input()
print(pali(n))