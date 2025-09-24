class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        

        n0, n1 = 2, 1  
        
        for i in range(3, n + 1):
            curr = n0 + n1
            n1 = n0
            n0 = curr
        
        return n0
