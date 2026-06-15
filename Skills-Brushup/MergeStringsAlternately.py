class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        # res = str()
        res = []
        while i < len(word1) and i < len (word2):
            
            # res.append(word1.charAt(i)) # 'str' object has no attribute 'charAt'
            # res.append(word2.charAt(i))
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        if i < len(word1):
            res.append (word1[i:])
            # i += 1

        if i < len(word2):
            res.append (word2[i:])
            # i += 1

        return "".join(res)
