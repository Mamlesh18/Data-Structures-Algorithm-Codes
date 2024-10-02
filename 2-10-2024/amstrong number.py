def ams(nums):
    convert_to_string = str(nums)
    total = 0
    i = 0
    while i < len(convert_to_string):
        a = int(convert_to_string[i]) ** 3
        total+=a
        i+=1
    if total == nums:
        return True
    else:
        return False
n = int(input())
print(ams(n))