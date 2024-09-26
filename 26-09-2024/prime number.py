def prime(nums):
    result = []
    for i in range(1,nums):
        if isprime(i):
            result.append(i)
    return result

def isprime(n):
    if n < 1:
        return
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input("enter"))
print(prime(n))