class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sub=[]
        for mask in range(1 << n):
            temp=[]
            for i in range(n):
                if ((mask >> i) & 1)==1:
                    temp.append(nums[i])
            sub.append(temp)
        return sub  
