def sub(s1,s2):

    i,j =0,0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            count+=1
            i+=1
        j+=1
    if count == len(s1):
        return True

    #
    #
    # if len(s2)< len(s1):
    #     return False
    #
    # stack = []
    # for i in range(0,len(s2)):
    #     stack.append(s2[i])
    # i = 0
    # count = 0
    # while i < len(s1):
    #     if s1[i] in stack:
    #         stack.remove(s1[i])
    #         count+=1
    #     i+=1
    # if count == len(s1):
    #     return True
    # else:
    #     return False
s1 = 'axc'
s2 = 'ahbgdc'
print(sub(s1,s2))

