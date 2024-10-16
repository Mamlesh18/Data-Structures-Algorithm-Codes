def palindrome(s):
    s = s.lower()
    temp = ''
    for i in range(0,len(s)):
        if not s[i].isalpha():
            continue
        temp+=s[i]
    if pali(temp):
        return True
    else:
        return False
def pali(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = "A man, a plan, a canal: Panama"
print(palindrome(s))
