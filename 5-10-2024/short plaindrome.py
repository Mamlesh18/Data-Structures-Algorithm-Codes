def short(s):
    if s == s[::-1]:
        return True
    else:
        return False

def shortest(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return s
    for i in range(len(s),0,-1):
        if short(s[:i]):
            sa = s[i:]
            return sa[::-1] + s

nums = 'abcd'
print(shortest(nums))
