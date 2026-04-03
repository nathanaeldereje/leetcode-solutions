class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i=0
        count=0
        stack=[]
        while i!=n and count<len(target):
            if i+1 == target[count]:
                stack.append('Push')
                count+=1
            else:
                stack.append('Push')
                stack.append('Pop')
                
            i+=1
        return stack
        
