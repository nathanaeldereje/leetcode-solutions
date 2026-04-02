class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_numbers = set(range(1, n + 1))
        set_nums=set(nums)
        return list(all_numbers - set_nums)


