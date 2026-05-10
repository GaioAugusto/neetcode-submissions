class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        c1,c2 = 0,0
        while c1 < len(word1) and c2 < len(word2):
            result += word1[c1]
            result += word2[c2]
            c1 += 1
            c2 += 1
        
        if c1 < len(word1):
            result += word1[c1:]
        
        else:
            result += word2[c2:]
        
        return result