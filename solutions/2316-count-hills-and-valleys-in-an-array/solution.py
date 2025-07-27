class Solution(object):
    def countHillValley(self, nums):
        count = 0
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1
            elif nums[i] == nums[i + 1]:
                previous_num = nums[i - 1]
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                if i + 1 < len(nums):
                    if nums[i] > previous_num and nums[i] > nums[i + 1]:
                        count += 1
                    elif nums[i] < previous_num and nums[i] < nums[i + 1]:
                        count += 1
            i += 1
        return count

sol = Solution()
print(sol.countHillValley([21,21,21,2,2,2,2,21,21,45]))

