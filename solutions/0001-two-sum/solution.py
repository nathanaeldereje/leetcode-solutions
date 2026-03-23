class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            j = seen.get(target - num)
            if j is not None:
                return [j, i]
            seen[num] = i
