# from collections import Counter
def count_characters(s: str) -> dict[str, int]:
    freq = {}
    for i in range (len(s)):
        freq [s[i]] = freq.get(s[i],0) + 1
    return freq

# using the Counter library
from collections import Counter
def count_characters(s: str) -> dict[str, int]:
    freq = Counter (s)
    return freq
