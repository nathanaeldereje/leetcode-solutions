class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l=max(len(a), len(b))
        a= a.zfill(l)
        b= b.zfill(l)
        carry=0
        chars=[]
        for i in range(l-1,-1,-1):
            sum=int(a[i])+int(b[i])+carry
            if sum==0:
                chars.append('0')
                carry=0
            elif sum==1:
                chars.append('1')
                carry=0
            elif sum==2:
                chars.append('0')
                carry=1
            else:
                chars.append('1')
                carry=1
        if carry:
            chars.append("1")
        return "".join(reversed(chars))





        
