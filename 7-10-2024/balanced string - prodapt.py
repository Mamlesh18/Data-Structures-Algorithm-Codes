def balanced(s1,s2):
    res = 0
    s1one = s1.count('1')
    s1zero = s1.count('0')
    s2one = s2.count('1')
    s2zero = s2.count('0')

    totalone = s1one + s2one
    totalzero = s1zero + s2zero
    if totalone == totalzero:
        return res
    i = 0
    j = len(s1)-1

    while i <= len(s1) and j >= 0:
        if totalone == totalzero:
            return res
        if j >= 0 and s1[j] == '1':
            s1one-=1
        elif j >=0 and s1[j] == '0':
            s1zero-=1
        res +=1
        j-=1

        if totalone == totalzero:
            return res
        if i <= len(s1)-1 and s1[i] == '1':
            s2one -=1
        elif i <=len(s1)-1 and s2[i] == '0':
            s2zero-=1
        res+=1
        i+=1
    return totalzero == totalone



s1 = '001'
s2 = '101'
print(balanced(s1,s2))