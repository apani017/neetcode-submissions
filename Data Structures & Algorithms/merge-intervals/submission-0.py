class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], end)]

        return merged