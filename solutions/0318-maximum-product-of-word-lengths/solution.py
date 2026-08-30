class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks=[]
        max_p=0
        for w in words:
            mask = 0
            for c in w:
                bit = ord(c) - ord('a')
                mask |= 1 << bit

            masks.append((mask, len(w)))
        
        words_l=len(words)
        for i in range(words_l):
            for j in range(i+1, words_l):
                if masks[i][1] * masks[j][1] <= max_p:
                    continue
                if (masks[i][0]&masks[j][0])==0:
                    max_p=(masks[i][1]*masks[j][1])
        return max_p





        
