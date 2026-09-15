class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        req = {}
        window = {}
        
        for c in s1:
            req[c] = req.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if (r-l+1) > len(s1):
                left = s2[l]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                l += 1
            if req == window:
                return True

        return False
            