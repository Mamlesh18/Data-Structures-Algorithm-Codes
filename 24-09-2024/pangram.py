def pangram(s):
    if len(s) < 25:
        return False
    s.lower()
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        if i in alphabets:
            alphabets.remove(i)
    if not alphabets:
        return True
    else:
        return False

s = input('string - ')
print(pangram(s))