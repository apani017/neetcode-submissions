class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        timeLeft = []

        for p, s in pair:
            timeLeft.append((target - p)/s)
            print(timeLeft)
            if len(timeLeft) >= 2 and timeLeft[-1] <= timeLeft[-2]:
                timeLeft.pop()
        return len(timeLeft)
        