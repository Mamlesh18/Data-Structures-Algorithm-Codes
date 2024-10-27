def findAnagrams(s,p):
        sliding = len(p)
        arr = list(p)
        i = 0
        result = []
        while i < len(s) - sliding + 1:
            total = s[i:i+sliding]
            j = 0
            arr2 = arr.copy()
            while j < len(total):
                if total[j] in arr2:
                    arr2.remove(total[j])
                j+=1
            if not arr2:
                result.append(i)
            i+=1
        return result

s = 'abcdacb'
p = 'abc'
print(findAnagrams(s,p))