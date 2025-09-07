# from typing import List
# import random

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2:
            res.append(0)
        # random.shuffle(res)
        return res

