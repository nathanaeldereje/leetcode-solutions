class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
        for i, char in enumerate(s):
            if dict[char] == 1:
                return i
        return -1

    
