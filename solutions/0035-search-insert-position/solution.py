class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=right//2
        while(left<=right):
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right=mid-1
                mid=(right+left)//2
            elif nums[mid]<target:
                left=mid+1
                mid=(right+left)//2
        return left

