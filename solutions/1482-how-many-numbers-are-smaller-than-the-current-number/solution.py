class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict={}
        smaller_nums=[]
        for i,num in enumerate(sorted_nums):
            if num not in dict:
                dict[num]=i
        for num in nums:
            smaller_nums.append(dict[num])
        return smaller_nums
