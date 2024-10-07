def reverse(s):
    if not s:
        return ''
    result = []
    temp = ''
    for i in range(0,len(s)):
        if s[i] == ' ':
            if temp:
                result.append(temp)
                temp = ''
        else:
            temp+=s[i]
    result.append(temp)
    ans = []
    for i in range(len(result)-1,-1,-1):
        ans.append(result[i])
    return ' '.join(ans)

s = 'the bluw is sku'
print(reverse(s))