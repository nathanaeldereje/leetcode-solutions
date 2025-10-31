from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write = 0
        for read in range(len(nums)):
            # allow if fewer than 2 written, or not creating a third duplicate
            if write < 2 or nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write

