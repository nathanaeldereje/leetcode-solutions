class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=0
        for num in nums:
            result^=num
        diff=result & (-result)
        num_a, num_b = 0, 0
        for num in nums:
            if num & diff == 0:
                num_a ^=num      
            else:
                num_b ^=num
        return [num_a,num_b]
        
