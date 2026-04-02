class Solution:
    def isClosing(self, char: str) -> bool:
        if char == ')' or char == ']' or char == '}':
            return True
        return False

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        openings = []
        for i in range(len(s)):
            if not self.isClosing(s[i]):
                openings.append(s[i])
            else:
                if not openings:
                    return False
                opening = openings.pop()
                if s[i] == ')' and opening != '(':
                    return False
                if s[i] == ']' and opening != '[':
                    return False
                if s[i] == '}' and opening != '{':
                    return False
        if openings:
            return False
        return True