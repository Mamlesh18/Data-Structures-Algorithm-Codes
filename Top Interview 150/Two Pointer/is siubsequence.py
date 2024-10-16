def subs(s1,s2):
    res2 = []
    i = 0
    while i < len(s1):
        res2.append(s1[i])
        i+=1
    j = 0
    print(res2)

    while j < len(s2):
        if s2[j] in res2:
            res2.remove(s2[j])
        j+=1
    if not res2:
        return True
    else:
        return False
s1 = 'abc'
s2 = 'ahbgdc'
print(subs(s1,s2))