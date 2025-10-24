class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums=len(nums)-1
        self.quicksort(nums,0,len_nums)
    def quicksort(self,array:List[int],start,end):
        if(start>=end):
            return #this is the base case
        
        pivot=self.partition(array,start,end)
        self.quicksort(array,start,pivot-1)
        self.quicksort(array,pivot+1,end)
    def partition(self,array:List[int],start,end):
        pivot=array[end]
        i=start-1
        for j in range(start,end):
            if(array[j]<pivot):
                i+=1
                array[i],array[j]=array[j],array[i]
        i+=1
        array[i],array[end]=array[end],array[i]
        return i

    
            

