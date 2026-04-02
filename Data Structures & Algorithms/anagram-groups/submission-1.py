class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            
            if key not in groups:
                groups[key] = []  # Initialize an empty list for new key

            groups[key].append(word)  # Now it's safe to append

        return list(groups.values())