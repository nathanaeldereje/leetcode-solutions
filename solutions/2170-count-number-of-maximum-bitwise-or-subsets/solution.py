from typing import List
from itertools import combinations
from functools import reduce

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        highest = reduce(lambda x, y: x | y, nums)
        count = 0
        size = len(nums)
        
        for r in range(1, size + 1):  # from 1 to size inclusive
            for combo in combinations(nums, r):
                result = reduce(lambda x, y: x | y, combo)
                if result > highest:
                    highest = result
                    count = 1
                elif result == highest:
                    count += 1
        
        return count

# -------- Test Code Below --------

solution = Solution()
test_input = [3,1]
result = solution.countMaxOrSubsets(test_input)
print("Output:", result)

