class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        val_list = []

        for i in range(0, len_nums - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[len_nums - 1] + nums[len_nums - 2] + nums[len_nums - 3] < target:
                continue
            for j in range(i + 1, len_nums - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len_nums - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        val_list.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1

        return val_list

