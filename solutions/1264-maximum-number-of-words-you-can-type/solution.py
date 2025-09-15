class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        count = 0
        for w in words:
            if broken.isdisjoint(w):  # ✅ True if no common letters
                count += 1
        return count

