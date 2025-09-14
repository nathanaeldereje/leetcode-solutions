from typing import List

class Solution:
    VOWELS = "aeiou"
    # Create a translation table to replace all vowels with '*'
    TRANSTABLE = str.maketrans({v: "*" for v in VOWELS})

    def devowel(self, word: str) -> str:
        # Lowercase once and translate all vowels
        return word.lower().translate(self.TRANSTABLE)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []

        exact_set = set(wordlist)
        lowercase_dict = {}
        devowel_dict = {}

        for word in wordlist:
            lower = word.lower()
            lowercase_dict.setdefault(lower, word)
            devowel_dict.setdefault(self.devowel(lower), word)

        for word in queries:
            lower_word = word.lower()
            if word in exact_set:
                result.append(word)
            elif lower_word in lowercase_dict:
                result.append(lowercase_dict[lower_word])
            else:
                devow_query = self.devowel(lower_word)
                result.append(devowel_dict.get(devow_query, ""))

        return result
