import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            v, i = heapq.heappop(heap)
            heapq.heappush(heap, (v * multiplier, i))

        result = [0] * len(nums)
        for v, i in heap:
            result[i] = v
        return result