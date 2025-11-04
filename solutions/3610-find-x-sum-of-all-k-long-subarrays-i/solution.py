from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            sorted_items = sorted(freq.items(), key=lambda t: (t[1], t[0]), reverse=True)
            top_x = {num for num, _ in sorted_items[:x]}
            s = sum(num for num in sub if num in top_x)
            res.append(s)
        return res
