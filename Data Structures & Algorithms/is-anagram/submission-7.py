class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # idea: traverse the first string, record all the characters and number of
        # occurrences. Then, traverse the second string and start removing from the dictionary.
        # if you find a character that is not in the dict, not an anagram. 
        # if dictionary is not empty at the end, not an anagram either.

        if len(s) != len(t):
            return False

        # first string
        characters = {}
        for char in s:
            if characters.get(char) is not None:
                characters[char] += 1
            else:
                characters[char] = 1

        # second string
        for char in t:
            # check if char exists
            if characters.get(char) is None:
                return False
            # remove from dictionary
            if characters[char] == 1:
                del characters[char]
            else:
                characters[char] -= 1
        return True