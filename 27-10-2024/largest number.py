from functools import cmp_to_key

def larger(nums):

    nums = list(map(str,nums))
    lar = sorted(nums,key = cmp_to_key(compare))
    return ''.join(lar)
def compare(x,y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
nums = list(map(int,input().split()))
print(larger(nums))