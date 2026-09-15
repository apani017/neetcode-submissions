class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            # shrink window to size len(s1)
            if r - l + 1 > len(s1):
                left_char = s2[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l += 1

            if window == need:
                return True

        return False
