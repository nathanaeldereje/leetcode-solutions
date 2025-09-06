class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        collection=[]

        def backtrack(path,used):
            if len(path)==len(nums):
                collection.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True

                    backtrack(path,used)
                    path.pop()
                    used[i]=False
            
        backtrack([],[False]*len(nums))
        return collection
