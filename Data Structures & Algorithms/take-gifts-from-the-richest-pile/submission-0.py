import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for i in range(k):
            heapq.heapreplace_max(gifts, int(math.sqrt(gifts[0])))

        result = 0
        for i in gifts:
            result += i
        return result