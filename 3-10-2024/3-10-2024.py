def canPlaceFlowers(flowerbed,n):
    stack = [1] * n
    for i in range(0, len(flowerbed)):
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = stack.pop()
    if not stack:
        return True
    else:
        return False

nums = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(nums,n))