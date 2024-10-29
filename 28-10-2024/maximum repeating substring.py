def maximum(s,t):
    count = 0
    temp = 0
    i = 0
    while i < len(s) - len(t):
        if s[i:i+len(t)] == t:
            count+=1
            i+=len(t)
        else:
            temp = max(temp,count)
            count=0
            i+=1

    temp= max(temp,count)
    return temp
s = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"

t = 'aaaba'
print(maximum(s,t))