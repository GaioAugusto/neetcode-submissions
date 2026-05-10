class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1, n2 = len(nums1), len(nums2)

        counter = 0
        for i in range(n1-n2, n1):
            nums1[i] = nums2[counter]
            counter += 1
        
        return nums1.sort()
