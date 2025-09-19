class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        empty = [-1, -1]
        loc = []

        if len(nums) == 0:
            return empty

        for x in range(len(nums)):
            if nums[x] == target:
                loc.append(x)

        if not loc:  # check if list is empty
            return empty
        else:
            return [loc[0], loc[-1]]  # first and last occurrence
