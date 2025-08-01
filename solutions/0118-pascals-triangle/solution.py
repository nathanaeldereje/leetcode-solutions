from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascals = [[1]]  
         # minimal fix
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, len(pascals[i-1])):
                temp.append(pascals[i-1][j] + pascals[i-1][j - 1])
            temp.append(1) 
            
            pascals.append(temp)
        return pascals 
