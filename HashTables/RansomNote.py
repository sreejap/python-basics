from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len (magazine):
            return False
            
        c1 = Counter (ransomNote)
        c2 = Counter (magazine)
        # aa, aab
        for c in c1:
            if c not in c2:
                return False
            if c1[c] > c2[c]:
                return False

        return True    

        
