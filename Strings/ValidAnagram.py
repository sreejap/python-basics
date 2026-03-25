class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        mapping = {}

        for i in range (len(s)):
            c1 = s[i]
            c2 = t[i]

            mapping [c1] = mapping.get(c1,0)+1            
            mapping [c2] = mapping.get(c2,0)-1            

        for char in mapping: # is this how we iterate the keys
            if mapping[char]!=0:
                return False
        
        return True
