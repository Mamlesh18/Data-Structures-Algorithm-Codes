def substring(s1,s2):
    if not s1 or not s2:
        return None

    count = 0
    res = 0
    for i in range(0,len(s1)):
        for j in range(i,len(s1)):
            total = s1[i:j]
            if total in s2 and len(total) > count:
                count = len(total)
                res = total

    return res,count

s1 = input('s1 ')
s2 = input('s2 ')
print(substring(s1,s2))