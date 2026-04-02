class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_location = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if numbers_location.get(complement) != None:
                return [numbers_location[complement], i]
            numbers_location[nums[i]] = i
        return False