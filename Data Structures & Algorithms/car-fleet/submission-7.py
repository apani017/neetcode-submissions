class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        res = []

        for p, s in cars:
            time = (target - p) / s

            if not res or time > res[-1]:
                res.append(time)
        
        return len(res)

