import heapq

class Solution:        
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones) # O(n) in-place operation

        while len(stones) > 1:
            s1 = stones[0]
            heapq.heappop_max(stones)
            s2 = stones[0]
            heapq.heappop_max(stones)

            s = abs(s2-s1)

            if s != 0:
                heapq.heappush_max(stones, s)
        return stones[0] if len(stones) != 0 else 0


