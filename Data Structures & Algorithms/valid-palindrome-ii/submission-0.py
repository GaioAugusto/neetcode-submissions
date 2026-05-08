class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    return False
            return True

        if is_palindrome(s):
            return True

        for i in range(len(s)-1):
            prefix = s[:i]
            suffix = s[i+1:]
            if is_palindrome(prefix+suffix):
                return True
        return False