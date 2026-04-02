class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Isolate target
        # nums[i] + nums[j] + nums[k] = 0
        # -nums[i] = nums[j] + nums[k]
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Found triplet
                if nums[left] + nums[right] == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return triplets