class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_chars = {}
        for char in t:
            if word_chars.get(char) == None:
                word_chars[char] = 1
            else:
                word_chars[char] += 1

        for char in s:
            if word_chars.get(char) == None:
                return False
            else:
                if word_chars[char] == 1:
                    del word_chars[char]
                else:
                    word_chars[char] -= 1
        return len(word_chars) == 0