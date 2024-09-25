def balanaced(nums):
    dicts = {'}':'{',']':'[',')':'('}
    stack = []
    for i in nums:
        if i in dicts.values():
            stack.append(i)
        if i in dicts.keys():
            if stack == [] or dicts[i]!=stack.pop():
                return False
    if not stack:
        return True
    else:
        return False
nums = input("para")
print(balanaced(nums))