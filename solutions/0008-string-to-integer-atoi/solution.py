class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()

        sgn=1
        if not s:
            return 0
        if s[0]=='-':
            sgn = -1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]


        nums=[]
        result = 0

        for char in s:
            if not char.isdigit():
                break

            result = result * 10 + ord(char) - ord('0')
        
        result = result * sgn

        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1

        return result


        
        
