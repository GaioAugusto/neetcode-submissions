class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr

        window_size=k
        l = 0
        for r in range(k, len(arr)):
            if abs(arr[r]-x) < abs(arr[l]-x):
                l = r - k + 1

        return arr[l:l+k]