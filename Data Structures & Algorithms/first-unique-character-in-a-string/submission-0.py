from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = OrderedDict()

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] = -1
            else:
                seen[s[i]] = i
        
        for letter, index in seen.items():
            if index >= 0:
                return index
        return -1