class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        result = digits

        carry = 1 if digits[i] == 9 else 0

        while i >= 0:
            if result[i] + carry < 10:
                result[i] += 1
                return result
            carry = 1
            result[i] = 0
            i -= 1

        return [1]+result