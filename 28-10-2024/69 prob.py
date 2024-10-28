def change(nums):
    s = str(nums)
    co = s
    result = []
    result.append(nums)
    for i in range(0,len(s)):
        if s[i] == '6':
            s = s[:i] + '9' + s[i+1:]
            result.append(int(s))
        else:
            s = s[:i] + '6' + s[i+1:]
            result.append(int(s))
        s = co

    return max(result)
nums = 6699
print(change(nums))
