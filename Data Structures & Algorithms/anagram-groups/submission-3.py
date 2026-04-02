class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            # alternative with strings not tuple
            # key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key] = []  # Initialize an empty list for new key

            groups[key].append(word)

        return list(groups.values())