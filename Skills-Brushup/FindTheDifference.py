# Counter returns 0 for missing keys. Understanding that behavior is exactly the kind of "basic Python" knowledge recruiters often mean when they mention Python questions.
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter (s)

        for ch in t:
            if counter_s[ch] == 0:
                return ch
            counter_s [ch] -= 1
