import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l<=r:
            m = (l+r)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/m)
            if hrs<=h:
                k = m
                r = m-1
            elif hrs>h:
                l = m+1
        return k