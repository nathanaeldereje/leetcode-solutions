class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l=len(columnTitle)
        result=0
        for i in range(l):
            result+=(26**(l-i-1))*(ord(columnTitle[i])-ord('A')+1)
        return result


