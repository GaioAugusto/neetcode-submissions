class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {} # Keys: actual values; values: indices
        for i in range(len(nums)):
            complement = target - nums[i]
            if numbers.get(complement) != None:
                return [numbers[complement], i]
            elif numbers.get(nums[i]) == None:
                numbers[nums[i]] = i
        return None