def counts(s1,s2):
    arr_s1 = []
    arr_s2 = []
    i = 0
    j = 0
    temp1 = ''
    temp2 = ''

    while i < len(s1):
        if s1[i] == ' ':
            arr_s1.append(temp1)
            temp1 = ''
            i+=1
        temp1 += s1[i]
        i+=1
    arr_s1.append(temp1)

    while j < len(s2):
        if s2[j] == ' ':
            arr_s2.append(temp2)
            temp2 = ''
            j+=1
        temp2 += s2[j]
        j+=1
    arr_s2.append(temp2)

    for k in arr_s2:
        if k in arr_s1:
            arr_s1.remove(k)
    print(arr_s1,arr_s2)
    return len(arr_s1)


s1 = 'hi i am program program'
s2 = 'hi i am program'
print(counts(s1,s2))
