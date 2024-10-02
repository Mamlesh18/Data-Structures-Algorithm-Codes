def leap(nums):
    if nums%4==0:
        return 'leap'
    else:
        return 'no'
n = int(input())
print(leap(n))