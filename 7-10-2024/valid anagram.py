def valid(s,t):
    if not s or not t or len(s) != len(t):
        return False
    stack = []
    for i in s:
        stack.append(i)
    for j in t:
        if j in stack:
            stack.remove(j)
    if not stack:
        return True
    else:
        return False
s = 'rat'
t = 'atr'
print(valid(s,t))
