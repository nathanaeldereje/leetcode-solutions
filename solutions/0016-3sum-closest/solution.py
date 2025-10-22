class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] 

        for i in range(len_nums - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len_nums - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

    
                if current_diff < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # exact match found

        return closest_sum

