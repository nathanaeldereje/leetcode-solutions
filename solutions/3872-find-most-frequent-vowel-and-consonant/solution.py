class Solution:
    def maxFreqSum(self, s: str) -> int:
        dict_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        dict_cons = {}
        vowels = "aeiou"

        for char in s:
            if char in vowels:
                dict_vowels[char] += 1
            else:
                if char.isalpha():
                    dict_cons[char] = dict_cons.get(char, 0) + 1

        max_vowel = max(dict_vowels.values()) if any(dict_vowels.values()) else 0
        max_cons  = max(dict_cons.values()) if dict_cons else 0

        return max_vowel + max_cons

