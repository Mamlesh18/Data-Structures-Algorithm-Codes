from functools import cmp_to_key
def cmpkeys(nums):
    arrays = sorted(nums,key = cmp_to_key(compare))
    res = ''.join(arrays)
    return res

def compare(x,y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return
    else:
        return 0

nums = list(map(str,input().split()))
print(cmpkeys(nums))