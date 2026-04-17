class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        for pile in piles:    
            if pile > k:
                k = pile
        
        #  mid -> current speed to test
        # compute time to consume all piles
        # if time < h, update l
        # else time > h, update k
        l = 1
        r = k
        while l <= r:
            mid = (l+r) // 2
            counter = 0
            for i in range(len(piles)):
                if piles[i] / mid < 1:
                    counter += 1
                elif piles[i] / mid != piles[i] // mid:
                    counter += 1 + piles[i] // mid
                else:
                    counter += piles[i] // mid
            if counter > h:
                l = mid+1
            else:
                r = mid-1
                k=mid
        return k
        
