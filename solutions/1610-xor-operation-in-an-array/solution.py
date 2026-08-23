class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        result=0
        for i in range(n):
            nums.append(start+2*i)
        for i in nums:
            result^=i
        return result


