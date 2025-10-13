import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        for left, right in zip(cleaned, reversed(cleaned)):
            if left != right:
                return False
        return True

