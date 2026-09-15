class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k : [1, max(piles)]
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l+r)//2
            t = 0
            for pile in piles:
                t += math.ceil(pile/k)

            if t <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
