class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            
            second=target-num
            if second in map.keys():
                return([map[second],i])
            if num not in map.keys():
                map[num]=i
        return container

            
