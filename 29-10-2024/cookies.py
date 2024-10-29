def cookie(s,t):
    s.sort(reverse=True)
    t.sort(reverse=True)
    i = 0
    j = 0
    count = 0
    while i < len(s) and j < len(t):
        if s[i] <= t[j]:
            count+=1
            j+=1
        i+=1
    return count

s = [1,2]
t = [1,2,3]
print(cookie(s,t))