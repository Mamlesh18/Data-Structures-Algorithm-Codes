def letters(s):
    if not s:
        return 0
    dicts ={ 2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    result = []
    strings = str(s)
    for i in range(len(strings)):
        if int(strings[i]) in dicts:
            result.append(dicts[int(strings[i])])
    return result

s = int(input())
print(letters(s))