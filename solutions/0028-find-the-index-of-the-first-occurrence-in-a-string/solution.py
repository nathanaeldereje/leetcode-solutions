class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        
        if len_needle > len_haystack:
            return -1
        
        pos_occ = []
        for k in range(len_haystack - len_needle + 1):  
            if haystack[k] == needle[0] and haystack[k + len_needle - 1] == needle[len_needle - 1]:
                pos_occ.append(k)

        for i in pos_occ:
            condition = True 
            for j in range(len_needle):
                if needle[j] != haystack[i + j]:
                    condition = False
                    break
            if condition:
                return i
        return -1

