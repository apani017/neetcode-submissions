class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = slow = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            eta = (target-p)/s
            if eta > slow:
                res += 1
                slow = eta
        return res