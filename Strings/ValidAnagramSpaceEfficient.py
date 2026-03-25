class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # count [] = [0] * 26  - no need
        count = [0] * 26

        for i in range (len(s)):
            count [ord(s[i]) - ord('a')] += 1
            count [ord(t[i]) - ord('a')] -= 1
        

        # for i in range(len(count)):
        #     if count[i]!=0:
        #         return False
        
        # return True

        return all ( c == 0 for c in count) # polished python code
