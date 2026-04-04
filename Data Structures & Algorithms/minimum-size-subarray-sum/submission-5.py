class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        left = 0
        min_len = len(nums)
        found_array = False
        for right in range(len(nums)):
            sum += nums[right]
            if sum >= target:
                found_array = True
                while sum >= target:
                    sum -= nums[left]
                    left += 1
                if right - left + 2 < min_len:
                    min_len = right - left + 2
                
        if found_array:
            return min_len
        return 0

# SUM: 15,10,17,7
# RIGHT: 4,5
# LEFT: 3,4,5
# LEN: 2,