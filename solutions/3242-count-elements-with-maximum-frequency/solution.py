class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict={}
        for _ in nums:
            dict[_]=dict.get(_,0)+1
        max_freq=max(dict.values())
        total = sum(count for count in dict.values() if count == max_freq)
        return total
