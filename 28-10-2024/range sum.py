class Range:
    def __init__(self,nums):
        self.stack = []
        for i in nums:
            self.stack.append(i)
    def sums(self,left,right):
        total = sum(self.stack[left:right+1])
        return total

nums = [1,2,3,4,5]
r = Range(nums)

print(r.sums(1,3))

