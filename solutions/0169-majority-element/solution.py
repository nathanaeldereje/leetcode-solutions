class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        most_common = nums[0]

        for num in counts:
            if counts[num] > counts[most_common]:
                most_common = num
        return most_common
                




        
