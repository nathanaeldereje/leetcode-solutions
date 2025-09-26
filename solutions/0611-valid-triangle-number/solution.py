class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        left=0
        right=0
        for i in range(len(nums) - 1, -1, -1):
            c = nums[i]

            left,right=0,i-1
            while left < right:
                if nums[left] + nums[right] > c:
                    count += right - left
                    right -= 1
                else:
                    left += 1


                
        return count
