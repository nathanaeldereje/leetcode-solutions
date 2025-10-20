class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        str_size=len(s)
        p=str_size-1
        for i in range(0,str_size//2):
            s[i],s[p]=s[p],s[i]
            p-=1
            
            
        
