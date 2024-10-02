def sumfibo(nums):
    if nums <= 0:
        return 0
    elif nums == 1:
        return 1
    else:
        a = sumfibo(nums-1) + sumfibo(nums-2)

        return a

def fibo(n):
    total = 0
    for i in range(n+1):
        total+=sumfibo(i)
    return total
nums = int(input())
print(fibo(nums))