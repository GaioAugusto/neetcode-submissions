class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_counter = {}
        for num in nums:
            if num in number_counter:
                number_counter[num] += 1
            else:
                number_counter[num] = 1

        current_best = [0, 0]
        for key, value in number_counter.items():
            if value > current_best[1]:
                current_best[0] = key
                current_best[1] = value
        return current_best[0]