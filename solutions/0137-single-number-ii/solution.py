class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_d={}
        for num in nums:
            nums_d[num] = nums_d.get(num, 0) + 1
        for num, count in nums_d.items():
            if count == 1:
                return num
        return 0
        
