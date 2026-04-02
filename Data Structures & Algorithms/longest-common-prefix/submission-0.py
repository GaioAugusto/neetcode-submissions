class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_smallest = strs[0]
        for s in strs:
            if len(s) < len(current_smallest):
                current_smallest = s

        prefix = current_smallest        
        for s in strs:
            for i in range(len(prefix)):
                if prefix[i] != s[i]:
                    prefix = prefix[0:i]
                    break

        return prefix