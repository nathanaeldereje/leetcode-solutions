from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort to handle duplicates

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # skip used or duplicate numbers at the same recursion level
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False]*len(nums))
        return res



