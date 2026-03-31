class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list=[]
        x=0
        y=n
        while(x!=n):
            new_list.append(nums[x])
            new_list.append(nums[y])
            x+=1
            y+=1
        return new_list
