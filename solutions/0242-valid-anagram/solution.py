class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict={}
        for i in s:
            count_dict[i] = count_dict.get(i, 0) + 1
        for char in t:
            if char not in count_dict:
                return False
            count_dict[char]-=1
        zeros=[0] * len(count_dict)
        # print(count_dict.values())
        return list(count_dict.values())==zeros

