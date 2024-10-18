def subs(s,t):
    if not s:
        return -1
    a = len(t)
    for i in range(0,len(s)):
        if s[i:i+a] == t:
            return i
    return -1


s = "butsad"
t = "sad"
print(subs(s,t))