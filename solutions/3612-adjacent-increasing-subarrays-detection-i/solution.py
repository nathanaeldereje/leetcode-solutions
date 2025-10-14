from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        curr_len = 1  
        prev_len = 0  
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                prev_len = curr_len
                curr_len = 1
            
            # Case 1: Current sequence is long enough for 2 adjacent k-subarrays
            if curr_len >= 2 * k:
                return True
            
            # Case 2: Previous and current sequences each have length >= k
            if curr_len >= k and prev_len >= k:
                return True
        
        return False
